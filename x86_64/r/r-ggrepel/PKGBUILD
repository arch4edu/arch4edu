# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=ggrepel
_pkgver=0.9.6
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
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
md5sums=('d84bbecfeb624fe1ec70f11712596b13')
b2sums=('1dfc8e152a02e55fe176996707cf08fa063921346179d7a42ed0d3f370f3f941af8478a9bace48f29a34bd87bd67584a3831eb5cdd4c1aab0e8c2d0d8fbddb3f')

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
