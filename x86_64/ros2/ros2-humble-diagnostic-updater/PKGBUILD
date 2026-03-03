# Maintainer: insmtr <insmtr@insmtr.cn>
# Contributor: Angelo Elias Dal Zotto <angelodalzotto97@gmail.com>

_pkgroot=diagnostics
_pkgname=diagnostic_updater
pkgname=ros2-humble-diagnostic-updater
pkgver=4.4.6
pkgrel=1
pkgdesc="diagnostic_updater contains tools for easily updating diagnostics"
url="https://index.ros.org/p/diagnostic_updater/"
arch=('any')
depends=(
    'ros2-humble' 
)
makedepends=('cmake' 'gcc13')
source=("https://github.com/ros/diagnostics/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('d574c494c15c50851b0a2a0044190a3472efa157a3ea257dc5e79691412a05e1')


build() {
    source /opt/ros/humble/setup.bash

    export CC=$(command -v gcc-13) CXX=$(command -v g++-13)

    cmake -B build -S "$_pkgroot-$pkgver/$_pkgname" \
        -DCMAKE_BUILD_TYPE='None' \
        -DCMAKE_INSTALL_PREFIX='/opt/ros/humble' \
        -Wno-dev
    
    cmake --build build
}

package() {
    DESTDIR="$pkgdir" cmake --install build
}
