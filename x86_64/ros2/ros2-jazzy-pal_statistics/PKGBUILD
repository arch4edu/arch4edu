# Maintainer: AutoUpdateBot <auto-update-bot@arch4edu.org>

pkgbase=ros2-jazzy-pal_statistics
pkgname=(
    'ros2-jazzy-pal_statistics_msgs'
    'ros2-jazzy-pal_statistics'
)
pkgver=2.8.2
pkgrel=1
pkgdesc="Statistics messages and utilities for ROS 2 Jazzy"
url="https://github.com/pal-robotics/pal_statistics"
arch=('x86_64')
license=('MIT')
depends=('ros2-jazzy')
makedepends=('cmake' 'boost')
source=("$pkgbase-$pkgver.tar.gz::https://github.com/pal-robotics/pal_statistics/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('a05368e58e3fd8c428a165f238c7a7e11b9368a985717b8acb7c353c83677021')

_srcname="pal_statistics-$pkgver"

_build_cmake() {
    local sub="$1"
    shift
    source /opt/ros/jazzy/setup.bash

    local prefix='' dep
    for dep in "$@"; do
        prefix+="$srcdir/stage-$dep/opt/ros/jazzy:"
    done

    CMAKE_PREFIX_PATH="${prefix}${CMAKE_PREFIX_PATH}" \
        cmake -B "$srcdir/build-$sub" -S "$srcdir/$_srcname/$sub" \
            -DCMAKE_BUILD_TYPE='None' \
            -DCMAKE_INSTALL_PREFIX='/opt/ros/jazzy' \
            -DBUILD_TESTING=OFF \
            -Wno-dev
    cmake --build "$srcdir/build-$sub"
    DESTDIR="$srcdir/stage-$sub" cmake --install "$srcdir/build-$sub"
}

build() {
    export CFLAGS+=" -ffile-prefix-map=$srcdir=/usr/src/debug/$pkgbase"
    export CXXFLAGS+=" -ffile-prefix-map=$srcdir=/usr/src/debug/$pkgbase"

    _build_cmake pal_statistics_msgs
    _build_cmake pal_statistics pal_statistics_msgs
}

package_ros2-jazzy-pal_statistics_msgs() {
    depends=('ros2-jazzy')
    cp -a "$srcdir/stage-pal_statistics_msgs/." "$pkgdir/"
    install -Dm644 "$srcdir/$_srcname/pal_statistics_msgs/LICENSE" \
        "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

package_ros2-jazzy-pal_statistics() {
    depends=('ros2-jazzy' 'ros2-jazzy-pal_statistics_msgs' 'boost' 'gcc-libs')
    cp -a "$srcdir/stage-pal_statistics/." "$pkgdir/"
    install -Dm644 "$srcdir/$_srcname/pal_statistics/LICENSE" \
        "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
