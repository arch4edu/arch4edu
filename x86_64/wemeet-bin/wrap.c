// by https://aur.archlinux.org/account/AvianaCruz
#ifndef _GNU_SOURCE
#define _GNU_SOURCE
#endif

#include <X11/Xlibint.h>
#include <dlfcn.h>
#include <openssl/ssl.h>
#include <stdlib.h>

#ifdef WRAP_FORCE_SINK_HARDWARE
#include <pulse/introspect.h>
#include <pulse/subscribe.h>
#include <string.h>
#endif

#ifdef SSL_get_peer_certificate
#undef SSL_get_peer_certificate
#endif

X509 *SSL_get_peer_certificate(const SSL *s) {
  return SSL_get1_peer_certificate(s);
}

// temporary hack for Wayland screen sharing crash
typedef int (*wrap_XMapWindow_t)(register Display *dpy, Window w);
static wrap_XMapWindow_t wrap_orig_XMapWindow;

int XMapWindow(register Display *dpy, Window w) {
  const char *env = getenv("XDG_SESSION_TYPE");
  if (env == NULL || strcmp(env, "wayland") != 0) {
    if (!wrap_orig_XMapWindow) {
      wrap_orig_XMapWindow = dlsym(RTLD_NEXT, "XMapWindow");
    }

    return wrap_orig_XMapWindow(dpy, w);
  }

  return 1;
}

#ifdef WRAP_FORCE_SINK_HARDWARE
typedef pa_operation *(*wrap_pa_get_sink_by_name_t)(pa_context *c,
                                                    const char *name,
                                                    pa_sink_info_cb_t cb,
                                                    void *userdata);
typedef pa_operation *(*wrap_pa_get_sink_by_index_t)(pa_context *c,
                                                     uint32_t idx,
                                                     pa_sink_info_cb_t cb,
                                                     void *userdata);
typedef pa_operation *(*wrap_pa_get_sink_list_t)(pa_context *c,
                                                 pa_sink_info_cb_t cb,
                                                 void *userdata);

static wrap_pa_get_sink_by_name_t wrap_orig_get_sink_info_by_name;
static pa_sink_info_cb_t wrap_orig_sink_info_by_name_cb;

static wrap_pa_get_sink_by_index_t wrap_orig_get_sink_info_by_index;
static pa_sink_info_cb_t wrap_orig_sink_info_by_index_cb;

static wrap_pa_get_sink_list_t wrap_orig_get_sink_list;
static pa_sink_info_cb_t wrap_orig_sink_info_list_cb;

static void wrap_get_sink_info_callback(pa_context *c, const pa_sink_info *i,
                                        int eol, void *userdata,
                                        pa_sink_info_cb_t orig_cb) {
  if (i && !(i->flags & PA_SINK_HARDWARE)) {
    pa_sink_info sink_info[sizeof(pa_sink_info)];
    memcpy(sink_info, i, sizeof(pa_sink_info));
    sink_info->flags |= PA_SINK_HARDWARE;

    orig_cb(c, sink_info, eol, userdata);
  } else {
    orig_cb(c, i, eol, userdata);
  }
}

static void wrap_get_sink_info_by_name_callback(pa_context *c,
                                                const pa_sink_info *i, int eol,
                                                void *userdata) {
  wrap_get_sink_info_callback(c, i, eol, userdata,
                              wrap_orig_sink_info_by_name_cb);
}

static void wrap_get_sink_info_by_index_callback(pa_context *c,
                                                 const pa_sink_info *i, int eol,
                                                 void *userdata) {
  wrap_get_sink_info_callback(c, i, eol, userdata,
                              wrap_orig_sink_info_by_index_cb);
}

static void wrap_get_sink_info_list_callback(pa_context *c,
                                             const pa_sink_info *i, int eol,
                                             void *userdata) {
  wrap_get_sink_info_callback(c, i, eol, userdata, wrap_orig_sink_info_list_cb);
}

pa_operation *pa_context_get_sink_info_list(pa_context *c, pa_sink_info_cb_t cb,
                                            void *userdata) {
  if (!wrap_orig_get_sink_list) {
    wrap_orig_get_sink_list = dlsym(RTLD_NEXT, "pa_context_get_sink_info_list");
  }
  wrap_orig_sink_info_list_cb = cb;

  return wrap_orig_get_sink_list(c, wrap_get_sink_info_list_callback, userdata);
}

pa_operation *pa_context_get_sink_info_by_index(pa_context *c, uint32_t idx,
                                                pa_sink_info_cb_t cb,
                                                void *userdata) {
  if (!wrap_orig_get_sink_info_by_index) {
    wrap_orig_get_sink_info_by_index =
        dlsym(RTLD_NEXT, "pa_context_get_sink_info_by_index");
  }
  wrap_orig_sink_info_by_index_cb = cb;

  return wrap_orig_get_sink_info_by_index(
      c, idx, wrap_get_sink_info_by_index_callback, userdata);
}

pa_operation *pa_context_get_sink_info_by_name(pa_context *c, const char *name,
                                               pa_sink_info_cb_t cb,
                                               void *userdata) {
  if (!wrap_orig_get_sink_info_by_name) {
    wrap_orig_get_sink_info_by_name =
        dlsym(RTLD_NEXT, "pa_context_get_sink_info_by_name");
  }
  wrap_orig_sink_info_by_name_cb = cb;

  return wrap_orig_get_sink_info_by_name(
      c, name, wrap_get_sink_info_by_name_callback, userdata);
}
#endif
