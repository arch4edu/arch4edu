# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=loo
_pkgver=2.8.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Efficient Leave-One-Out Cross-Validation and WAIC for Bayesian Models"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-or-later')
depends=(
  pandoc
  r-checkmate
  r-matrixstats
  r-posterior
)
optdepends=(
  r-bayesplot
  r-brms
  r-ggplot2
  r-knitr
  r-rmarkdown
  r-rstan
  r-rstanarm
  r-rstantools
  r-spdep
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('95f122c54c58c9079d5349748e58d75a')
b2sums=('3453168f21dfc3963abe8bea7d2b212cf6aa903a547b3309a5939a234c38f47d52c6ca6b3e373e406ba2113d5ff90c1c64a34d8ce063bc56a613f86645b72dac')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
