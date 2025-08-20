# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Nick B <Shirakawasuna at gmail _dot_com>

_pkgname=effects
_pkgver=4.2-4
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
md5sums=('e8eb6970e1ed9e52cd18a537de6bbd06')
b2sums=('d04d879abca85f3553447c668c852399ed775fbe0b04ab7cd67048e914e5ba808610228147c9682188bbef040859fca649eae4187e542c43642dd0721451158d')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
