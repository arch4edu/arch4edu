# Maintainer: AutoUpdateBot <auto-update-bot@arch4edu.org>

_pkgname=qt_gui_cpp
pkgname=ros2-jazzy-qt_gui_cpp
pkgver=2.7.6
pkgrel=1
pkgdesc="ROS 2 qt_gui_cpp - C++ bindings for the qt_gui plugin framework"
url="https://index.ros.org/p/qt_gui_cpp/"
arch=('x86_64')
license=('BSD-3-Clause')
depends=('ros2-jazzy' 'qt5-base')
makedepends=('cmake' 'pkgconf' 'qt5-base' 'sip4' 'python-sip4' 'python-pyqt5')
source=("qt_gui_core-$pkgver.tar.gz::https://github.com/ros-visualization/qt_gui_core/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('da49feedc9e48101bab48c7d4efe13879cee26db485df27b03fa00de9652c49b')

_srcname="qt_gui_core-$pkgver"

build() {
    source /opt/ros/jazzy/setup.bash

    cmake -B build -S "$srcdir/$_srcname/$_pkgname" \
        -DCMAKE_BUILD_TYPE='None' \
        -DCMAKE_INSTALL_PREFIX='/opt/ros/jazzy' \
        -DBUILD_TESTING=OFF \
        -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
        -Wno-dev
    cmake --build build
}

package() {
    DESTDIR="$pkgdir" cmake --install build
    install -Dm644 "$srcdir/$_srcname/LICENSE" \
        "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
