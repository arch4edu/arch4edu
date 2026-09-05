# Maintainer: AutoUpdateBot <auto-update-bot@arch4edu.org>

_pkgname=realtime_tools
pkgname=ros2-jazzy-realtime_tools
pkgver=3.12.0
pkgrel=1
pkgdesc="Contains realtime-safe tools to share data between hard-realtime and other threads, for ROS 2 Jazzy"
url="https://github.com/ros-controls/realtime_tools"
arch=('x86_64')
license=('BSD-3-Clause')
depends=('ros2-jazzy' 'boost-libs' 'libcap' 'fmt')
makedepends=('cmake' 'boost' 'ros2-jazzy-ros2_control_cmake')
source=("$pkgname-$pkgver.tar.gz::https://github.com/ros-controls/realtime_tools/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('2c0e60bf69b614bb98732fd042b142b82972799a68fef7e5e94e160bec386671')

_srcname="realtime_tools-$pkgver"

build() {
    source /opt/ros/jazzy/setup.bash

    export CFLAGS+=" -ffile-prefix-map=$srcdir=/usr/src/debug/$pkgname"
    export CXXFLAGS+=" -ffile-prefix-map=$srcdir=/usr/src/debug/$pkgname"

    cmake -B build -S "$_srcname/$_pkgname" \
        -DCMAKE_BUILD_TYPE='None' \
        -DCMAKE_INSTALL_PREFIX='/opt/ros/jazzy' \
        -DBUILD_TESTING=OFF \
        -Wno-dev
    cmake --build build
}

package() {
    DESTDIR="$pkgdir" cmake --install build

    install -Dm644 "$_srcname/LICENSE" \
        "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
