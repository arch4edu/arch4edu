# Maintainer: dhn <neilson+aur@sent.com>
# Contributor: Robert Greener <me@r0bert.dev>

_pkgname=gdata
pkgname=r-$_pkgname
pkgver=2.18.0.1
pkgrel=1
pkgdesc='Various R Programming Tools for Data Manipulation'
arch=('any')
url="https://cran.r-project.org/web/packages/$_pkgname/"
license=('GPL2')
depends=('r' 'r-gtools')
makedepends=()
optdepends=('perl-spreadsheet-parsexlsx')
source=("https://cran.r-project.org/src/contrib/${_pkgname}_$pkgver.tar.gz")
sha512sums=('f51f3d4289237fea7b981318da015969956c793f3882ffca553e08dde56bc3e38bff23de2becbe613a9b19d3e390d0597bcc753e51a504285be8268372f6ebe7')

build(){
    R CMD INSTALL ${_pkgname}_$pkgver.tar.gz -l "$srcdir"
}

package() {
    install -dm 755 "$pkgdir"/usr/lib/R/library
    cp -a --no-preserve=ownership ${_pkgname} "$pkgdir"/usr/lib/R/library
}
