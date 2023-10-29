# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=mstate
_pkgver=0.3.2
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Data Preparation, Estimation and Prediction in Multi-State Models"
arch=(x86_64)
url="https://cran.r-project.org/package=${_pkgname}"
license=(GPL)
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
sha256sums=('3c473dff6854e31cdbdaf79f8fe7eaf97119b01a581874a894b283555afe8d14')

build() {
  mkdir -p build
  R CMD INSTALL "$_pkgname" -l build
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
