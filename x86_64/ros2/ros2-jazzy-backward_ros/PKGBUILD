# Maintainer: AutoUpdateBot <auto-update-bot@arch4edu.org>

_pkgname=backward_ros
pkgname=ros2-jazzy-backward_ros
pkgver=1.0.8
pkgrel=1
pkgdesc="ROS 2 wrapper around backward-cpp for pretty stack traces on crashes"
url="https://github.com/pal-robotics/backward_ros"
arch=('x86_64')
license=('MIT')
depends=('ros2-jazzy' 'elfutils')
makedepends=('cmake')
source=("$_pkgname-$pkgver.tar.gz::https://github.com/pal-robotics/backward_ros/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('cfcfe150f2290cc5899b22463379c879c1c3eb0a09d3ad9b26f6b292d67b51a8')

build() {
    source /opt/ros/jazzy/setup.bash

    export CFLAGS+=" -ffile-prefix-map=$srcdir=/usr/src/debug/$pkgname"
    export CXXFLAGS+=" -ffile-prefix-map=$srcdir=/usr/src/debug/$pkgname"

    cmake -B build -S "$srcdir/$_pkgname-$pkgver" \
        -DCMAKE_BUILD_TYPE='None' \
        -DCMAKE_INSTALL_PREFIX='/opt/ros/jazzy' \
        -DBUILD_TESTING=OFF \
        -Wno-dev
    cmake --build build
}

package() {
    DESTDIR="$pkgdir" cmake --install build
    install -Dm644 "$srcdir/$_pkgname-$pkgver/LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
