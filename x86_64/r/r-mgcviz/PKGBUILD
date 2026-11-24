# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=mgcViz
_pkgver=0.2.3
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
md5sums=('a7c4f8bfb0e3996c301ce34edca06c89')
b2sums=('4b8a95fe57e99202c3a3c9a40081cd26965f8ab88b915a00019523b5b518977b0a2827874cf61043d9ae3e4e278e41c09664bb62b16d30f3c4952a7e084fe5e3')

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
