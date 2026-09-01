# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=bbmle
_pkgver=1.0.26
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Tools for General Maximum Likelihood Estimation"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-bdsmatrix
  r-mvtnorm
  r-numderiv
)
optdepends=(
  r-aiccmodavg
  r-emdbook
  r-ggplot2
  r-hmisc
  r-knitr
  r-minqa
  r-mumin
  r-optimx
  r-rms
  r-runit
  r-testthat
  r-tinytest
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('91c6fdb5331d44e6e6035e11997b3338')
b2sums=('0c2c8a333f824eb62442bf43a6883dcbc2c02a535ce1273b391bdc12bd3fdd19223a11119f8e120e0170fd56ab39e435aa5149d43bb4fac521cb1b6c6c5e5ca0')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
