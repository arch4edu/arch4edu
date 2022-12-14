# Maintainer: dhn <neilson+aur@sent.com>
# Contributor: Robert Greener <me@r0bert.dev>

_pkgname=gtools
pkgname=r-$_pkgname
pkgver=3.9.4
pkgrel=1
pkgdesc='Various R Programming Tools'
arch=('any')
url="https://cran.r-project.org/web/packages/$_pkgname/"
license=('GPL2')
depends=('r')
makedepends=()
optdepends=()
source=("https://cran.r-project.org/src/contrib/${_pkgname}_$pkgver.tar.gz")
sha512sums=('3bebb121e91888ae4ff841ef7f0a215ffde2ca229531faf68b5311e438350627e5476e8367370f33c08883f5c3915a5724773c7028ffe23eab0728a37fd44b9f')

build(){
    R CMD INSTALL ${_pkgname}_$pkgver.tar.gz -l "$srcdir"
}

package() {
    install -dm 755 "$pkgdir"/usr/lib/R/library
    cp -a --no-preserve=ownership ${_pkgname} "$pkgdir"/usr/lib/R/library
}
