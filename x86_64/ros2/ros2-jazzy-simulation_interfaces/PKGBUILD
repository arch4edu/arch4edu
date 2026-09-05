# Maintainer: AutoUpdateBot <auto-update-bot@arch4edu.org>

_pkgname=simulation_interfaces
pkgname=ros2-jazzy-simulation_interfaces
pkgver=1.5.1
pkgrel=1
pkgdesc="ROS 2 simulation interfaces including messages, services and actions"
url="https://index.ros.org/p/simulation_interfaces/"
arch=('x86_64')
license=('Apache-2.0')
makedepends=('cmake')
depends=('ros2-jazzy')
source=("$_pkgname-$pkgver.tar.gz::https://github.com/ros-simulation/simulation_interfaces/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('01fa77266765c538338b7efc8058316fd4e4f0d0c9b504719d688b76394e332c')

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
