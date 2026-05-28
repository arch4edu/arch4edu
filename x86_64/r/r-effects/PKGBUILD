# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Nick B <Shirakawasuna at gmail _dot_com>

_pkgname=effects
_pkgver=4.2-5
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
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
md5sums=('3fcd08fced1ca2b96578701f8bf1699a')
b2sums=('a1dd776ad2fc9cb5a882f33133d9c9afe5c80db66e6004949e2e3bb2c4b39464d5e64940261eedaa1bc5e756d86aa959a440a62166d4e118354704574bc244a7')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
