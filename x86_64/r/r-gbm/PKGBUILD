# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=gbm
_pkgver=2.3.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Generalized Boosted Regression Models"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r
)
optdepends=(
  r-bookdown
  r-gridextra
  r-knitr
  r-pdp
  r-rmarkdown
  r-runit
  r-testthat
  r-viridis
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('1f0f31fed5e246d71bf999f486250c50')
b2sums=('06447f5c6e3ab9ca8dbf472e91b340903fb9f4abc5cadd4751bea4e37613cafaa5b5e8bd09dda591b1b18dea371ac8dbd567d43c89f437e32f0d7b3c370f5535')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
