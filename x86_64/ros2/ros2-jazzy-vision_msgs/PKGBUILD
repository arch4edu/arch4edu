# Maintainer: AutoUpdateBot <auto-update-bot@arch4edu.org>

pkgbase=ros2-jazzy-vision_msgs
pkgname=(
    'ros2-jazzy-vision_msgs'
    'ros2-jazzy-vision_msgs_rviz_plugins'
)
pkgver=4.1.1
pkgrel=1
pkgdesc="ROS 2 messages for common computer vision tasks"
url="https://index.ros.org/p/vision_msgs/"
arch=('x86_64')
license=('Apache-2.0')
depends=('ros2-jazzy')
makedepends=('cmake' 'python-numpy')
source=("$pkgbase-$pkgver.tar.gz::https://github.com/ros-perception/vision_msgs/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('1f54c590e5195dc3112e682eaf0abab47d244bc739e61102bdf183a8fe79f124')

_srcname="vision_msgs-$pkgver"

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

    _build_cmake vision_msgs
    _build_cmake vision_msgs_rviz_plugins vision_msgs
}

package_ros2-jazzy-vision_msgs() {
    pkgdesc="ROS 2 messages for common computer vision tasks"
    depends=('ros2-jazzy')

    cp -a "$srcdir/_staging/vision_msgs/." "$pkgdir/"
    install -Dm644 "$srcdir/$_srcname/LICENSE" \
        "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

package_ros2-jazzy-vision_msgs_rviz_plugins() {
    pkgdesc="RViz plugins for visualizing vision_msgs"
    depends=('ros2-jazzy' 'ros2-jazzy-vision_msgs' 'python-numpy')

    cp -a "$srcdir/_staging/vision_msgs_rviz_plugins/." "$pkgdir/"
    install -Dm644 "$srcdir/$_srcname/LICENSE" \
        "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
