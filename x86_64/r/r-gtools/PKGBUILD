# Maintainer: dhn <neilson+aur@sent.com>
# Contributor: Robert Greener <me@r0bert.dev>

_pkgname=gtools
pkgname=r-$_pkgname
pkgver=3.9.3
pkgrel=1
pkgdesc='Various R Programming Tools'
arch=('any')
url="https://cran.r-project.org/web/packages/$_pkgname/"
license=('GPL2')
depends=('r')
makedepends=()
optdepends=()
source=("https://cran.r-project.org/src/contrib/${_pkgname}_$pkgver.tar.gz")
sha512sums=('dd2aae84923e37865eaf02f5df47ddd449a14f526613a26abd1f92f9462641f5d698dba9a0270addc21eb3868cdd0f197d58bf329b2c01ae4207e5f10f55e543')

build(){
    R CMD INSTALL ${_pkgname}_$pkgver.tar.gz -l "$srcdir"
}

package() {
    install -dm 755 "$pkgdir"/usr/lib/R/library
    cp -a --no-preserve=ownership ${_pkgname} "$pkgdir"/usr/lib/R/library
}
