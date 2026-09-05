# Maintainer: AutoUpdateBot <auto-update-bot@arch4edu.org>

_pkgname=rqt_gui_cpp
pkgname=ros2-jazzy-rqt_gui_cpp
pkgver=1.6.4
pkgrel=1
pkgdesc="ROS 2 rqt_gui_cpp - C++ plugin support for the rqt GUI framework"
url="https://index.ros.org/p/rqt_gui_cpp/"
arch=('x86_64')
license=('BSD-3-Clause')
depends=('ros2-jazzy' 'ros2-jazzy-qt_gui_cpp' 'qt5-base')
makedepends=('cmake' 'qt5-base')
source=("rqt-$pkgver.tar.gz::https://github.com/ros-visualization/rqt/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('fae29a3d3e2ff63d34103ff52e6aefa8b1e0415d9c82494f452a9b6e1238f915')

_srcname="rqt-$pkgver"

build() {
    source /opt/ros/jazzy/setup.bash

    cmake -B build -S "$srcdir/$_srcname/$_pkgname" \
        -DCMAKE_BUILD_TYPE='None' \
        -DCMAKE_INSTALL_PREFIX='/opt/ros/jazzy' \
        -DBUILD_TESTING=OFF \
        -Wno-dev
    cmake --build build
}

package() {
    DESTDIR="$pkgdir" cmake --install build
    install -Dm644 "$srcdir/$_srcname/LICENSE" \
        "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
