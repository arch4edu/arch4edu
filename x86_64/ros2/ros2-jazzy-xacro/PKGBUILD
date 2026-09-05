# Maintainer: AutoUpdateBot <auto-update-bot@arch4edu.org>

_pkgname=xacro
pkgname=ros2-jazzy-xacro
pkgver=2.1.1
pkgrel=1
pkgdesc="Xacro (XML Macros) - an XML macro language for ROS"
url="https://index.ros.org/p/xacro/"
arch=('any')
license=('BSD-3-Clause')
makedepends=('cmake' 'python-setuptools')
depends=('ros2-jazzy' 'python-yaml')
source=("$_pkgname-$pkgver.tar.gz::https://github.com/ros/xacro/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('f9d94956574015427e59011d4ee113b206e9c10a27a0c01d4b08ee4268d76741')

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
