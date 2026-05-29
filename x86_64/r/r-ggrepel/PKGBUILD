# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=ggrepel
_pkgver=0.9.8
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
  r-s7
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
  r-marquee
  r-patchwork
  r-prettydoc
  r-readr
  r-rmarkdown
  r-sf
  r-stringr
  r-rsvg
  r-svglite
  r-testthat
  r-vdiffr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('33e4c1f39e92d9e828203b10e12f831c')
b2sums=('f95b2aa520c6fdf650508d94231fa603a2434000d924fa19111d3ee3595a06c46a6948b80af91f7e9604a232888118976c872bf2b0d69f6751a5db5d67d61b85')

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
