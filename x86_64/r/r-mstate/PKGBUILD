# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=mstate
_pkgver=0.3.2
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=3
pkgdesc="Data Preparation, Estimation and Prediction in Multi-State Models"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-data.table
  r-rcolorbrewer
  r-rlang
  r-viridislite
)
optdepends=(
  r-cmprsk
  r-ggplot2
  r-knitr
  r-relsurv
  r-rmarkdown
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('14aab86d42cc542dd73c96e279119ca9')
b2sums=('19841c61413db8eae0a7419bc27726e02825095a7f9df04fb4c44e5d021f23e3ff6552f07930894c3d27cd8950d41e4eefbabea7d6119cb7906adc8c0ae9bbe1')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
