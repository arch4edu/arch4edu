# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=Brobdingnag
_pkgver=1.2-9
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=5
pkgdesc="Very Large Numbers in R"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=(GPL)
depends=(
  r
)
optdepends=(
  r-cubature
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('0933a3366ef2f614998e8feee06473cc')
b2sums=('2fa605c4a16fe95fa169f61f301ddcef16ecc8d0e87498fd409d23db4e9541291902f610afe93e18b932edfe49d11aa738ccd39a51e62e5b7962d1659d2f0860')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
