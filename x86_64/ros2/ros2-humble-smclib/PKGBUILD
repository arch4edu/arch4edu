# Maintainer: Angelo Elias Dal Zotto <angelodalzotto97@gmail.com>

_pkgroot=bond_core
_pkgname=smclib
pkgname=ros2-humble-smclib
pkgver=3.0.2
pkgrel=4
pkgdesc="Converts a language-independent description of a state machine into the source code to support that state machine."
url="https://index.ros.org/p/smclib/"
arch=('any')
depends=(
    'ros2-humble' 
)
makedepends=('cmake')
source=("https://github.com/ros/bond_core/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('16f0a741c238057146c50f4537d0e41c6c1842f7890a9fea1e782743ec9909f3')


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
