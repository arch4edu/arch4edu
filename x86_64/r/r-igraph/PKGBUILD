# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Alex Branham <branham@utexas.edu>
# Contributor: Phil Schaf <flying-sheep@web.de>
# Contributor: Oleg Smirnov <oleg.smirnov@gmail.com>

_pkgname=igraph
_pkgver=1.5.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
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
  r-lifecycle
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
        "fix-test-snapshots.patch"
        "igraph-system-libs.patch")
md5sums=('c4a753bfe2eac76eccc3aaa6786e2fa1'
         '1ffe5fc15f4fe62b1f5c6f0bbe72bd23'
         '3863e3b0e1f9356f607103096c0b011c')
sha256sums=('add90a1e77ad4a5d95641f0556553e3f1d1c4443cb2d5afb70171efd278ab14a'
            'f7b1987927ab31a3c3749dd1c1195d725935430dec3a7cef06283d70e7ac377a'
            '4a910e3248983dc27f3306eb3b260988cb592d4dd806f73e0a77aa8aca2a5068')

prepare() {
  # fix test snapshots
  patch -Np1 -i fix-test-snapshots.patch

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
