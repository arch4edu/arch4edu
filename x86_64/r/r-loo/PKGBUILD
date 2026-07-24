# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=loo
_pkgver=2.10.1
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
md5sums=('6c0b2fb996c29a509f96c983e34fefe9')
b2sums=('397574f6cc5349c9884a504bb04f0eea09ed5fd677e00332fbfcdbf4e273378ddecc9e570001c975250249aa4fbffe2d728a65834c889057f63dbd990a5aa630')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
