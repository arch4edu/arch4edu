# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=randomizr
_pkgver=2.0.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Easy-to-Use Tools for Common Forms of Random Assignment and Sampling"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r-rcpp
)
optdepends=(
  r-balancedsampling
  r-blocktools
  r-declaredesign
  r-dplyr
  r-estimatr
  r-fabricatr
  r-ggplot2
  r-knitr
  r-purrr
  r-readr
  r-rmarkdown
  r-sampling
  r-testthat
  r-tidyr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('b5f5986f70836d372470bfa9bcd1b113')
b2sums=('76daa1f17020cedcea52fb92e0b8a7dbff2a2e786c0953fd53b89b18a331a7885202e064df5e75bed8a70cda5e3cef1b946777e3203ae4b4b2f30e23d87d2ad9')

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
