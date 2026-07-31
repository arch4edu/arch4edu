# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=poorman
_pkgver=0.2.8
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="A Poor Man's Dependency Free Recreation of 'dplyr'"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r
)
optdepends=(
  r-knitr
  r-rmarkdown
  r-roxygen2
  r-tinytest
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('a53cc3f1a1f58f1d078e28ce9eed0dae')
b2sums=('84f4bb2b3ae40ac11f85cd47b054bad0ce408b1cbcca364bd08ff67004cbfd4c5eb48624db2faafd7500f69d2280cfff11f97313c2d22bebce6928b5713f8c08')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"

  install -d "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "/usr/lib/R/library/$_pkgname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"
}
