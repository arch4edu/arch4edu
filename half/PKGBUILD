# Maintainer: acxz <akashpatel2008 at yahoo dot com>
pkgname=half
pkgver=2.1.0
pkgrel=1
pkgdesc="Half-precision floating-point library"
url="http://half.sourceforge.net/"
arch=(x86_64)
license=('MIT')
makedepends=()
depends=()
source=("${pkgname}-${pkgver}::https://sourceforge.net/projects/half/files/half/2.1.0/half-2.1.0.zip/download")
sha256sums=("ad1788afe0300fa2b02b0d1df128d857f021f92ccf7c8bddd07812685fa07a25")

package() {
    mkdir -p ${pkgdir}/usr/include/half
    cp ${srcdir}/include/half.hpp ${pkgdir}/usr/include/half
}
