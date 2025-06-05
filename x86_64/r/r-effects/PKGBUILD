# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Nick B <Shirakawasuna at gmail _dot_com>

_pkgname=effects
_pkgver=4.2-2
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=4
pkgdesc="Effect Displays for Linear, Generalized Linear, and Other Models"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-cardata
  r-colorspace
  r-estimability
  r-insight
  r-lme4
  r-survey
)
optdepends=(
  r-alr4
  r-betareg
  r-car
  r-heplots
  r-knitr
  r-ordinal
  r-pbkrtest
  r-polca
  r-robustlmm
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('cdcae07573da34746bfa4c246a6c4502')
b2sums=('37520b6e13f68f1d9684e714695ef25b39ba241bfbec8f8956d0efbdc2a36536621095a65908b181a7e170a1869f483418d473b4ae215411e1273c2038163f82')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
