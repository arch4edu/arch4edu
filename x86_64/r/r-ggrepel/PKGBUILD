# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=ggrepel
_pkgver=0.9.4
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="Automatically Position Non-Overlapping Text Labels with 'ggplot2'"
arch=(x86_64)
url="https://cran.r-project.org/package=${_pkgname}"
license=(GPL3)
depends=(
  r-ggplot2
  r-rcpp
  r-rlang
  r-scales
  r-withr
)
checkdepends=(
  r-testthat
  r-vdiffr
  ttf-font
)
optdepends=(
  r-devtools
  r-dplyr
  r-ggbeeswarm
  r-gridextra
  r-knitr
  r-magrittr
  r-prettydoc
  r-readr
  r-rmarkdown
  r-stringr
  r-svglite
  r-testthat
  r-vdiffr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('80614592620fcaa8a11f99995ecec94b')
sha256sums=('81abb47270593709587480ffbc88dce3d3f695bd6f1164729311b37c50d7cf3e')

build() {
  mkdir -p build
  R CMD INSTALL "$_pkgname" -l build
}

check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" NOT_CRAN=true Rscript --vanilla testthat.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
