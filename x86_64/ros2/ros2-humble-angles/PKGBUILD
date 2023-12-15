# Maintainer: Angelo Elias Dal Zotto <angelodalzotto97@gmail.com>

_pkgname=angles
pkgname=ros2-humble-angles
pkgver=1.16.0
pkgrel=3
pkgdesc="This package provides a set of simple math utilities to work with angles"
url="https://index.ros.org/p/angles/"
arch=('any')
makedepends=('python-setuptools' 'cmake')
depends=('ros2-humble')
source=("https://github.com/ros/angles/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('25f5294d688e2e21583aa5e7fea64476f6a4a88ba59030b695f9d33682874efd')

build() {
    source /opt/ros/humble/setup.bash

    cmake -B build -S "$_pkgname-$pkgver/$_pkgname" \
        -DCMAKE_BUILD_TYPE='None' \
        -DCMAKE_INSTALL_PREFIX='/opt/ros/humble' \
        -Wno-dev
    
    cmake --build build
}

package() {
    DESTDIR="$pkgdir" cmake --install build
}
