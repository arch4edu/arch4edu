# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=mstate
_pkgver=0.3.3
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
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
md5sums=('50c0e638d55cf2ac953160b02a6db8ad')
b2sums=('6f3c221c844e54d4c64b0b5f330348e4537d2352812297aca9cf013615ea9cf2e4de60628aaedc8ca3db4186d7ef6838fe1f6322235bd547060b0287e621420d')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
