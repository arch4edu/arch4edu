# Maintainer: AutoUpdateBot <auto-update-bot@arch4edu.org>

_pkgname=ackermann_msgs
pkgname=ros2-jazzy-ackermann_msgs
pkgver=2.0.2
pkgrel=1
pkgdesc="Messages for Ackermann-steered vehicles, for ROS 2 Jazzy"
url="https://github.com/ros-drivers/ackermann_msgs"
arch=('x86_64')
license=('BSD-3-Clause')
depends=('ros2-jazzy')
makedepends=('cmake')
source=("$pkgname-$pkgver.tar.gz::https://github.com/ros-drivers/ackermann_msgs/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('26321df1bc2855adbcefac0a32091ce843271d93791fceff914a3f4c7b06d269')

build() {
    source /opt/ros/jazzy/setup.bash

    export CFLAGS+=" -ffile-prefix-map=$srcdir=/usr/src/debug/$pkgname"
    export CXXFLAGS+=" -ffile-prefix-map=$srcdir=/usr/src/debug/$pkgname"

    cmake -B build -S "$_pkgname-$pkgver" \
        -DCMAKE_BUILD_TYPE='None' \
        -DCMAKE_INSTALL_PREFIX='/opt/ros/jazzy' \
        -DBUILD_TESTING=OFF \
        -Wno-dev
    cmake --build build
}

package() {
    DESTDIR="$pkgdir" cmake --install build
}
