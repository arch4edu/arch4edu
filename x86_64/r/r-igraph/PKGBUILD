# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Alex Branham <branham@utexas.edu>
# Contributor: Phil Schaf <flying-sheep@web.de>
# Contributor: Oleg Smirnov <oleg.smirnov@gmail.com>

_pkgname=igraph
_pkgver=2.0.1.1
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
  plfit
  r-cli
  r-lifecycle
  r-magrittr
  r-pkgconfig
  r-rlang
  util-linux-libs
)
makedepends=(
  gcc-fortran
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
md5sums=('eb05121b1c41105eff1ec879a9d2701e'
         'c1733746148c001f363a5ef88c6c0bc6')
b2sums=('c28a109985d670578ae962aa24405258e09d18bdda86b83bf1bc36f26a6fea927b852f2f39e1044c43e7e3dacdc00f952ae1351b4c6b752df36bca2c243dbc52'
        '3a5f0e5f8821054733d71ddef66e9c734cd06bbd1d6f8f81fb718b1cf82cdb8cff300fab1622817b2716ad5860efd98e8995ce53c39ba153544a80838e89e4fd')

prepare() {
  # Build using system libraries
  patch -Np1 -i igraph-system-libs.patch
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
