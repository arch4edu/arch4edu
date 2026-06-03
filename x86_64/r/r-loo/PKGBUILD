# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=loo
_pkgver=2.9.0
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
md5sums=('165a31dc52f9b5ee989ff1e5739614a6')
b2sums=('826d022bba1cfd4d9ebca762bdc125b4dfbc371ddaceb90c0b25779decac5c3230c9dcf460c791c153dc94fa190ad00533055d788b24b92dda61816b34d648ee')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
