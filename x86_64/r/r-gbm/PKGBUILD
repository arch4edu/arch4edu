# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=gbm
_pkgver=2.3.0
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
md5sums=('311c5398b761011b808996bf4f31f250')
b2sums=('ace93618594bd7ecdae405d0719d277d6019cd4536df2abc205a6455a42f6d4a5b5ea5ac6f9f2736fb6d246117958eca1491f02397ffb846d297952a250845e7')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
