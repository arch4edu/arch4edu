#!/bin/sh
set -eu
export QT_AUTO_SCREEN_SCALE_FACTOR=1
export QT_STYLE_OVERRIDE=fusion                # 解决使用自带 Qt 情况下，字体颜色全白看不到的问题
export IBUS_USE_PORTAL=1                       # fix ibus
export LD_LIBRARY_PATH="/usr/lib/wemeet:$PATH" # 否则启动失败
USER_RUN_DIR="/run/user/$(id -u)"
CONFIG_DIR="${XDG_CONFIG_HOME:-$HOME/.config}"
FONTCONFIG_DIR="$CONFIG_DIR/fontconfig"
KDE_GLOBALS_FILE="$CONFIG_DIR/kdeglobals"
KDE_ICON_CACHE_FILE="${XDG_CACHE_HOME:-$HOME/.cache}/icon-cache.kcache"
WEMEET_APP_DIR="${XDG_DATA_HOME:-$HOME/.local/share}/wemeetapp"
LD_PRELOAD_WRAP="${LD_PRELOAD:-}:/usr/lib/wemeet/libwemeetwrap.so" # 用于缓解传输文件崩溃问题

export QT_QPA_PLATFORM=xcb
export XDG_SESSION_TYPE=x11
unset WAYLAND_DISPLAY
export WEMEET_XWAYLAND=1

if [ -f /usr/bin/bwrap ]; then
    mkdir -p "$WEMEET_APP_DIR"
    exec bwrap \
        --new-session \
        --unshare-user-try --unshare-pid --unshare-uts --unshare-cgroup-try \
        --ro-bind / / \
        --dev-bind /dev /dev \
        --bind /tmp /tmp \
        --ro-bind /dev/null /proc/cpuinfo \
        --tmpfs /sys/devices/virtual \
        --bind "$USER_RUN_DIR" "$USER_RUN_DIR" \
        --tmpfs /var \
        --tmpfs "$CONFIG_DIR" \
        --ro-bind-try "$KDE_GLOBALS_FILE" "$KDE_GLOBALS_FILE" \
        --ro-bind-try "$FONTCONFIG_DIR" "$FONTCONFIG_DIR" \
        --bind-try "$KDE_ICON_CACHE_FILE" "$KDE_ICON_CACHE_FILE" \
        --bind "$WEMEET_APP_DIR" "$WEMEET_APP_DIR" \
        --setenv LD_PRELOAD "$LD_PRELOAD_WRAP" \
        /opt/wemeet/bin/wemeetapp "$@"
else
    export LD_PRELOAD="$LD_PRELOAD_WRAP"
    exec /opt/wemeet/bin/wemeetapp "$@"
fi
