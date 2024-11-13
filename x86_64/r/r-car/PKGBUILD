# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Francois Garillot <francois[@]garillot.net>
# Contributor: Nick B <Shirakawasuna at gmail _dot_com>

_pkgname=car
_pkgver=3.1-3
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Companion to Applied Regression"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-abind
  r-cardata
  r-formula
  r-lme4
  r-pbkrtest
  r-quantreg
  r-scales
)
optdepends=(
  r-alr4
  r-coxme
  r-effects
  r-knitr
  r-leaps
  r-lmtest
  r-matrixmodels
  r-mvtnorm
  r-ordinal
  r-plotrix
  r-rgl
  r-rio
  r-sandwich
  r-sparsem
  r-survey
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('9103307ef76967da60b98da4f26f9ee9')
b2sums=('7419e1734d04cbb26bf693e6e88f84cdd233966d0c301b5b249a5121d2d1c4dc9c3ad2f7b4bd6332010a15fcafd38b05221b95f833661b0afa04b2caa4029f74')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
