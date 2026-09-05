# Maintainer: AutoUpdateBot <auto-update-bot@arch4edu.org>

_pkgname=filters
pkgname=ros2-jazzy-filters
pkgver=2.2.2
pkgrel=1
pkgdesc="Standardized interfaces for processing data as a sequence of filters, for ROS 2 Jazzy"
url="https://github.com/ros/filters"
arch=('x86_64')
license=('BSD-3-Clause')
depends=('ros2-jazzy' 'boost')
makedepends=('cmake')
source=("$pkgname-$pkgver.tar.gz::https://github.com/ros/filters/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('91f5d45f9f973103dcedecce13eea9a03c9e423ef60886250b37b8e45a2bbfc3')

prepare() {
    sed -n '1,28p' "$_pkgname-$pkgver/include/filters/filter_base.hpp" > LICENSE
}

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
    install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
