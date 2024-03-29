# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Alex Branham <branham@utexas.edu>
# Contributor: Phil Schaf <flying-sheep@web.de>
# Contributor: Oleg Smirnov <oleg.smirnov@gmail.com>

_pkgname=igraph
_pkgver=2.0.3
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Network Analysis and Visualization"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
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
  r-vctrs
  util-linux-libs
)
makedepends=(
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
md5sums=('36b28af2a8910060551629b306165f75'
         '5a958a08aa13c94de5820924a5e964ad')
b2sums=('3cc8510e01db17a4f5dffd43b9dbbe2e01d9e631289efcadcacecd8a577555cca2848eebb68299147e22618bd0e96691b2fc0a5eb0a59c549af66dc5c0d7ef25'
        'd2bd23dc816abfc33908b5583ee1129981fdccb8cd8b067cfb46e41f89d346135353ed6525467f14333064b601ae8544d0fa14931c34594bfdbcbcf45edf7c4b')

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
