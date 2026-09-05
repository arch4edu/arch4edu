# Maintainer: AutoUpdateBot <auto-update-bot@arch4edu.org>

pkgbase=ros2-jazzy-gps_umd
pkgname=(
    'ros2-jazzy-gps_msgs'
    'ros2-jazzy-gps_tools'
    'ros2-jazzy-gpsd_client'
    'ros2-jazzy-gps_umd'
)
pkgver=3.1.1
pkgrel=1
pkgdesc="ROS 2 GPS drivers and message definitions"
url="https://github.com/swri-robotics/gps_umd"
arch=('x86_64')
license=('BSD-3-Clause')
depends=('ros2-jazzy')
makedepends=('cmake' 'pkgconf' 'gpsd')
source=("$pkgbase-$pkgver.tar.gz::https://github.com/swri-robotics/gps_umd/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('fa5f550c141a1412b633c072b0b6ea352b977050383506e75dff50f9436ee9ec')

_srcname="gps_umd-$pkgver"

_build_cmake() {
    local _sub="$1"
    shift

    source /opt/ros/jazzy/setup.bash

    local _prefix='' _dep
    for _dep in "$@"; do
        _prefix+="$srcdir/_staging/$_dep/opt/ros/jazzy:"
    done

    CMAKE_PREFIX_PATH="${_prefix}${CMAKE_PREFIX_PATH}" \
        cmake -B "$srcdir/build-$_sub" -S "$srcdir/$_srcname/$_sub" \
            -DCMAKE_BUILD_TYPE='None' \
            -DCMAKE_INSTALL_PREFIX='/opt/ros/jazzy' \
            -DBUILD_TESTING=OFF \
            -Wno-dev
    cmake --build "$srcdir/build-$_sub"
    DESTDIR="$srcdir/_staging/$_sub" cmake --install "$srcdir/build-$_sub"
}

build() {
    rm -rf "$srcdir/_staging"

    # rosidl generators embed __FILE__ of generated sources into the shared
    # libraries; remap the build path so no $srcdir reference is retained.
    export CFLAGS+=" -ffile-prefix-map=$srcdir=/usr/src/debug/$pkgbase"
    export CXXFLAGS+=" -ffile-prefix-map=$srcdir=/usr/src/debug/$pkgbase"

    _build_cmake gps_msgs
    _build_cmake gps_tools gps_msgs
    _build_cmake gpsd_client gps_msgs
    _build_cmake gps_umd gps_msgs gps_tools gpsd_client
}

package_ros2-jazzy-gps_msgs() {
    pkgdesc="ROS 2 GPS message definitions"
    depends=('ros2-jazzy')

    cp -a "$srcdir/_staging/gps_msgs/." "$pkgdir/"
    install -Dm644 "$srcdir/$_srcname/LICENSE" \
        "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

package_ros2-jazzy-gps_tools() {
    pkgdesc="Python utilities for working with GPS data in ROS 2"
    depends=('ros2-jazzy' 'ros2-jazzy-gps_msgs' 'python')

    cp -a "$srcdir/_staging/gps_tools/." "$pkgdir/"
    install -Dm644 "$srcdir/$_srcname/LICENSE" \
        "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

package_ros2-jazzy-gpsd_client() {
    pkgdesc="ROS 2 client node for the gpsd GPS daemon"
    depends=('ros2-jazzy' 'ros2-jazzy-gps_msgs' 'gpsd')

    cp -a "$srcdir/_staging/gpsd_client/." "$pkgdir/"
    install -Dm644 "$srcdir/$_srcname/LICENSE" \
        "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

package_ros2-jazzy-gps_umd() {
    pkgdesc="Metapackage pulling in the full gps_umd stack"
    depends=('ros2-jazzy-gps_msgs' 'ros2-jazzy-gps_tools' 'ros2-jazzy-gpsd_client')

    cp -a "$srcdir/_staging/gps_umd/." "$pkgdir/"
    install -Dm644 "$srcdir/$_srcname/LICENSE" \
        "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
