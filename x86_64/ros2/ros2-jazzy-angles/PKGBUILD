# Maintainer: AutoUpdateBot <auto-update-bot@arch4edu.org>
# Contributor: insmtr <insmtr@insmtr.cn>
# Contributor: Angelo Elias Dal Zotto <angelodalzotto97@gmail.com>

_pkgname=angles
pkgname=ros2-jazzy-angles
pkgver=1.16.1
pkgrel=1
pkgdesc="This package provides a set of simple math utilities to work with angles"
url="https://index.ros.org/p/angles/"
arch=('any')
license=('BSD-3-Clause')
makedepends=('cmake' 'python-setuptools')
depends=('ros2-jazzy')
source=("$_pkgname-$pkgver.tar.gz::https://github.com/ros/angles/archive/${pkgver}.tar.gz")
sha256sums=('2bd37cba18f7cc4003712ad951237fb3cff5cc6d2bfd59a12ce3c558170e5fc2')

build() {
    source /opt/ros/jazzy/setup.bash

    cmake -B build -S "$_pkgname-$pkgver/$_pkgname" \
        -DCMAKE_BUILD_TYPE='Release' \
        -DCMAKE_INSTALL_PREFIX='/opt/ros/jazzy' \
        -Wno-dev

    cmake --build build
}

package() {
    DESTDIR="$pkgdir" cmake --install build

    # Upstream ships no LICENSE file; the BSD notice only exists as a comment
    # block at the top of the public header.
    sed -n '/Software License Agreement/,/POSSIBILITY OF SUCH DAMAGE/p' \
        "$_pkgname-$pkgver/$_pkgname/include/angles/angles.h" \
        | sed 's|^\*\{0,1\} \{0,2\}||' > LICENSE
    install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
