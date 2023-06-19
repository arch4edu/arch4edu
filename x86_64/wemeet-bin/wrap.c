// by https://aur.archlinux.org/account/AvianaCruz
#include <openssl/ssl.h>

#ifdef WRAP_FORCE_SINK_HARDWARE
#include <dlfcn.h>
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
