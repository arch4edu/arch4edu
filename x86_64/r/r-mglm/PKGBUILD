# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=MGLM
_pkgver=0.2.3
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Multivariate Response Generalized Linear Models"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r
)
optdepends=(
  r-ggplot2
  r-knitr
  r-plyr
  r-reshape2
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('29c738062a58e01686f01a3787d81446')
b2sums=('e601aac636bda198d7573aba97f0902930ccfa0ffa00f8ce709912197fd5a6ea93f7af873d56a3c3cef883000c3904cb4f136a25fbdc749a04623de7ad90eca2')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
