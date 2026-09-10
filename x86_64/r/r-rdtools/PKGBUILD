# Maintainer: Jingbei Li <i@jingbei.li>
_cranname=rdtools
_pkgver=0.1.0
pkgname=r-rdtools
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Efficient Manipulation of 'Rd' Files and Help Topics"
arch=('x86_64')
url="https://cran.r-project.org/package=${_cranname}"
license=('MIT')
depends=('r')
optdepends=('r-testthat: run the test suite'
            'r-withr: run the test suite')
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_pkgver}.tar.gz")
sha256sums=('90fdaef0c78ad322ca76f4b401c68b4028c2437cd51a1b6ccbf411d9c66c094b')

build() {
	R CMD INSTALL "${_cranname}_${_pkgver}.tar.gz" -l "$srcdir"
}

package() {
	install -dm0755 "$pkgdir/usr/lib/R/library"
	cp -a --no-preserve=ownership "${_cranname}" "$pkgdir/usr/lib/R/library"
	install -Dm0644 "${_cranname}/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
