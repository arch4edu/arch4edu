# Maintainer: AutoUpdateBot <auto-update-bot@arch4edu.org>

_pkgname=actuator_msgs
pkgname=ros2-jazzy-actuator_msgs
pkgver=0.0.1
pkgrel=1
pkgdesc="ROS 2 message interface for Actuators"
url="https://index.ros.org/p/actuator_msgs/"
arch=('x86_64')
license=('Apache-2.0')
makedepends=('cmake')
depends=('ros2-jazzy')
source=("$_pkgname-$pkgver.tar.gz::https://github.com/rudislabs/actuator_msgs/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('82ae5b5a3f7c3359a7164c140dd6ad7768aeec1836c97f5e750beb3182ccd695')

build() {
    source /opt/ros/jazzy/setup.bash

    cmake -B build -S "$_pkgname-$pkgver" \
        -DCMAKE_BUILD_TYPE='None' \
        -DCMAKE_INSTALL_PREFIX='/opt/ros/jazzy' \
        -DBUILD_TESTING=OFF \
        -Wno-dev

    cmake --build build
}

package() {
    DESTDIR="$pkgdir" cmake --install build

    install -Dm644 "$_pkgname-$pkgver/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
