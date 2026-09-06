# Maintainer: AutoUpdateBot <auto-update-bot@arch4edu.org>

_pkgname=rsl
pkgname=ros2-jazzy-rsl
pkgver=1.3.0
pkgrel=1
pkgdesc="ROS Support Library for ROS 2 Jazzy"
url="https://github.com/PickNikRobotics/RSL"
arch=('x86_64')
license=('BSD-3-Clause')
depends=(
    'ros2-jazzy'
    'ros2-jazzy-tcb_span'
    'tl-expected'
    'eigen'
    'fmt'
)
makedepends=('cmake')
source=("$pkgname-$pkgver.tar.gz::https://github.com/PickNikRobotics/RSL/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('14f2cdded6239d8dd498d1a8b7861227b7412af1f6374e9058c16adf2687dfcd')

_srcname="RSL-$pkgver"

build() {
    source /opt/ros/jazzy/setup.bash

    export CFLAGS+=" -ffile-prefix-map=$srcdir=/usr/src/debug/$pkgname"
    export CXXFLAGS+=" -ffile-prefix-map=$srcdir=/usr/src/debug/$pkgname"

    cmake -B build -S "$_srcname" \
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
