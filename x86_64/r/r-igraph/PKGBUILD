# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=igraph
_pkgver=1.5.0.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Network Analysis and Visualization"
arch=(x86_64)
url="https://cran.r-project.org/package=${_pkgname}"
license=(GPL)
depends=(
  arpack
  blas
  glpk
  gmp
  lapack
  libxml2
  plfit
  r-cli
  r-magrittr
  r-pkgconfig
  r-rlang
  suitesparse
  util-linux-libs
)
makedepends=(
  r-cpp11
)
checkdepends=(
  r-graph
  r-testthat
  r-vdiffr
)
optdepends=(
  r-ape
  r-callr
  r-decor
  r-digest
  r-graph
  r-igraphdata
  r-knitr
  r-rgl
  r-rmarkdown
  r-scales
  r-testthat
  r-vdiffr
  r-withr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz"
        "igraph-system-libs.patch")
md5sums=('9809e51f7a65bbb6ae45a480228a8d04'
         '34283a0a206240ab1f33f83d2526ffca')
sha256sums=('a80a157ee290252f89c7c690654d82eadf72eba389d3100da26a5bf2eb0da3b4'
            '38731c656da7f1fe34a4d21c3e3dcae65592898ba81620b96cd27c7894539530')

prepare() {
  cd "$_pkgname"
  # Build using system libraries
  patch -Np1 -i ../igraph-system-libs.patch
  autoconf
}

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
