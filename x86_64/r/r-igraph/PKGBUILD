# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Alex Branham <branham@utexas.edu>
# Contributor: Phil Schaf <flying-sheep@web.de>
# Contributor: Oleg Smirnov <oleg.smirnov@gmail.com>

_pkgname=igraph
_pkgver=2.2.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Network Analysis and Visualization"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  blas
  glpk
  gmp
  lapack
  libxml2
  r-cli
  r-lifecycle
  r-magrittr
  r-pkgconfig
  r-rlang
  r-vctrs
  util-linux-libs
)
makedepends=(
  gcc-fortran
  r-cpp11
)
checkdepends=(
  r-graph
  r-rgl
  r-testthat
  r-vdiffr
)
optdepends=(
  r-ape
  r-callr
  r-decor
  r-digest
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
        "igraph-system-libs20251202.patch")
md5sums=('09c2e2b0bd6b370e0b625b5a661afa39'
         '4f7de12ace8af846bafcfe0358f00dd3')
b2sums=('d63c12872675eaa729e6d058b163ddf7e557ee1ee22566f8b6221c7a52a0543decb37b8b2cc6dd4090b0f75214e0190c4bcf80fb8564ce8cc3f55d6879387b35'
        '1570ec5fd587860871962d5bf7a2c718b52e6b904a41d084f0df911f289d743bca51d6acc3d7e75f4faebeeb812cf869b2fb2eec20651f6b4ebb854e0935cb36')

prepare() {
  # Build using system libraries
  patch -Np1 -i igraph-system-libs20251202.patch
}

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
