# Maintainer: Angelo Elias Dal Zotto <angelodalzotto97@gmail.com>

_pkgroot=diagnostics
_pkgname=diagnostic_updater
pkgname=ros2-humble-diagnostic-updater
pkgver=3.1.2
pkgrel=2
pkgdesc="diagnostic_updater contains tools for easily updating diagnostics"
url="https://index.ros.org/p/diagnostic_updater/"
arch=('any')
depends=(
    'ros2-humble' 
)
makedepends=('cmake')
source=("https://github.com/ros/diagnostics/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('3944f6a8c4ba3574ebc0baf7d53f1a94c7a875ed07b9e0c1e070ccea08bff361')


build() {
    source /opt/ros/humble/setup.bash

    cmake -B build -S "$_pkgroot-$pkgver/$_pkgname" \
        -DCMAKE_BUILD_TYPE='None' \
        -DCMAKE_INSTALL_PREFIX='/opt/ros/humble' \
        -Wno-dev
    
    cmake --build build
}

package() {
    DESTDIR="$pkgdir" cmake --install build
}
