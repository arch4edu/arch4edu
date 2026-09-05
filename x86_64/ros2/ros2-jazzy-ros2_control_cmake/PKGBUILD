# Maintainer: AutoUpdateBot <auto-update-bot@arch4edu.org>

_pkgname=ros2_control_cmake
pkgname=ros2-jazzy-ros2_control_cmake
pkgver=0.4.0
pkgrel=1
pkgdesc="CMake macros used by the ros2_control framework, for ROS 2 Jazzy"
url="https://github.com/ros-controls/ros2_control_cmake"
arch=('any')
license=('Apache-2.0')
depends=('ros2-jazzy')
makedepends=('cmake')
source=("$pkgname-$pkgver.tar.gz::https://github.com/ros-controls/ros2_control_cmake/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('db384ae8e1490396ca9b4290b064c68a675bc07e4173cfbe28bcad93ada1c4ed')

_srcname="ros2_control_cmake-$pkgver"

build() {
    source /opt/ros/jazzy/setup.bash

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
