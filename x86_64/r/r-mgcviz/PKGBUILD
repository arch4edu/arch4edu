# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=mgcViz
_pkgver=0.2.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Visualisations for Generalized Additive Models"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-only')
depends=(
  r-gamm4
  r-ggally
  r-ggplot2
  r-gridextra
  r-matrixstats
  r-plyr
  r-qgam
  r-viridis
)
checkdepends=(
  r-hexbin
  r-testthat
)
optdepends=(
  r-knitr
  r-rgl
  r-rmarkdown
  r-testthat
  r-webshot2
  r-shiny
  r-miniui
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('5f3a5fa196c9b19df7cfddcb0b368564')
b2sums=('660c70633fd063fbcbefbedb69227e1dcc28a56e7da2d151839ef632a2f009b20b7d36864b4d735c23be0e6a983e7c18923275b0e09c6a642d9ce7cfd97b90e9')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" NOT_CRAN=true Rscript --vanilla testthat.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
