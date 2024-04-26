# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=ggrepel
_pkgver=0.9.5
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="Automatically Position Non-Overlapping Text Labels with 'ggplot2'"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-only')
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
  r-ggpp
  r-gridextra
  r-knitr
  r-magrittr
  r-patchwork
  r-prettydoc
  r-readr
  r-rmarkdown
  r-stringr
  r-svglite
  r-testthat
  r-vdiffr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('07e2c7cac82ce345ea35ca0522c72ea9')
b2sums=('e99c226e6a269202ccd3ce78a12cf867afa435d7a1afa724e486492aaa74104011a6a7081c3f8ec8284de073d69b01e304318c512075be095ef47c994757d791')

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
