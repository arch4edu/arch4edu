# Maintainer: Guilhem Saurel <guilhem.saurel@laas.fr>

_org='coal-library'
_pkgname='coal'
pkgname=("$_pkgname" "$_pkgname-docs")
pkgver=3.0.4
pkgrel=1
pkgdesc="Detection Library, previously known as hpp-fcl"
arch=('i686' 'x86_64')
url="https://github.com/$_org/$_pkgname"
license=('BSD-2-Clause')
depends=('assimp' 'eigen' 'eigenpy' 'octomap' 'qhull' 'python-numpy' 'boost-libs' 'python' 'glibc' 'gcc-libs')
optdepends=('doxygen')
makedepends=('cmake' 'boost')
conflicts=('hpp-fcl')
replaces=('hpp-fcl')
source=("${pkgname}-${pkgver}.tar.gz::$url/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('0a4f58e55b88a3d9f873ce79979aecc08491d212ea0b9311df013df3b22bffac')

build() {
    cmake -B "build-$pkgver" -S "$pkgbase-$pkgver" \
        -DCOAL_BACKWARD_COMPATIBILITY_WITH_HPP_FCL=ON \
        -DCOAL_HAS_QHULL=ON \
        -DCMAKE_CTEST_ARGUMENTS="-E;coal-bvh_models" \
        -DCMAKE_INSTALL_LIBDIR=lib \
        -DCMAKE_INSTALL_PREFIX=/usr \
        -DINSTALL_DOCUMENTATION=ON \
        -DBUILD_DOCUMENTATION=ON \
        -Wno-dev
    cmake --build "build-$pkgver"
}

check() {
    cmake --build "build-$pkgver" -t test
}

package_coal() {
    DESTDIR="$pkgdir/" cmake --build "build-$pkgver" -t install
    rm -rf "$pkgdir/usr/share/doc"
    install -Dm644 "$pkgbase-$pkgver/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

package_coal-docs() {
    DESTDIR="$pkgdir/" cmake --build "build-$pkgver" -t install
    rm -rf "$pkgdir"/usr/{lib,include,share/{"$_pkgname",ament_index}}
    install -Dm644 "$pkgbase-$pkgver/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
