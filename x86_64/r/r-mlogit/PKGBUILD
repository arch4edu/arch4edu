# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=mlogit
_pkgver=2.0-0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Multinomial Logit Models"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-dfidx
  r-formula
  r-lmtest
  r-micsr
  r-numderiv
  r-rdpack
)
optdepends=(
  r-aer
  r-car
  r-dplyr
  r-ggplot2
  r-knitr
  r-quarto
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('11500eb6d984e33e9e898274188ad450')
b2sums=('100c7ae82777536883530d652ac8dc34856202497e4cecfe4d2a5c47e57de02984a441bb5a43c0fef02873c7bf2d80dbd8ad505a9a8dc2db094c05fd43018d39')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
