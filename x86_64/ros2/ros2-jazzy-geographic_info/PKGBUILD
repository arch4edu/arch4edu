# Maintainer: AutoUpdateBot <auto-update-bot@arch4edu.org>

pkgbase=ros2-jazzy-geographic_info
pkgname=(
    'ros2-jazzy-geographic_msgs'
    'ros2-jazzy-geodesy'
    'ros2-jazzy-geographic_info'
)
pkgver=1.0.6
pkgrel=1
pkgdesc="ROS 2 geographic information messages and geodesy utilities"
url="https://github.com/ros-geographic-info/geographic_info"
arch=('x86_64')
license=('BSD-3-Clause')
depends=('ros2-jazzy')
makedepends=('cmake' 'ros2-jazzy-angles' 'python-catkin_pkg')
source=("$pkgbase-$pkgver.tar.gz::https://github.com/ros-geographic-info/geographic_info/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('7ae385951816abde470463b0b7ed24ad5e4dce2d8c6a2f120e42e337b013ae18')

_srcname="geographic_info-$pkgver"

_gen_license() {
    sed -n '/Software License Agreement/,/POSSIBILITY OF SUCH DAMAGE/p' \
        "$srcdir/$_srcname/geodesy/tests/test_wgs84.cpp" \
        | sed 's|^\*\{0,1\} \{0,2\}||' > "$srcdir/LICENSE"
}

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
    _gen_license

    export CFLAGS+=" -ffile-prefix-map=$srcdir=/usr/src/debug/$pkgbase"
    export CXXFLAGS+=" -ffile-prefix-map=$srcdir=/usr/src/debug/$pkgbase"

    _build_cmake geographic_msgs
    _build_cmake geodesy geographic_msgs
    _build_cmake geographic_info geographic_msgs geodesy
}

package_ros2-jazzy-geographic_msgs() {
    pkgdesc="ROS 2 messages for geographic information systems"
    depends=('ros2-jazzy')

    cp -a "$srcdir/_staging/geographic_msgs/." "$pkgdir/"
    install -Dm644 "$srcdir/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

package_ros2-jazzy-geodesy() {
    pkgdesc="ROS 2 geodesy utilities for converting geographic coordinates"
    depends=('ros2-jazzy' 'ros2-jazzy-angles' 'ros2-jazzy-geographic_msgs' 'python-pyproj' 'python-catkin_pkg')

    cp -a "$srcdir/_staging/geodesy/." "$pkgdir/"
    install -Dm644 "$srcdir/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

package_ros2-jazzy-geographic_info() {
    pkgdesc="Metapackage for ROS 2 geographic information"
    depends=('ros2-jazzy-geographic_msgs' 'ros2-jazzy-geodesy')

    cp -a "$srcdir/_staging/geographic_info/." "$pkgdir/"
    install -Dm644 "$srcdir/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
