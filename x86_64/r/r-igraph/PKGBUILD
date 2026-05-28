# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Alex Branham <branham@utexas.edu>
# Contributor: Phil Schaf <flying-sheep@web.de>
# Contributor: Oleg Smirnov <oleg.smirnov@gmail.com>

_pkgname=igraph
_pkgver=2.3.1
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
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
#        "igraph-system-libs20251202.patch")
md5sums=('c35002b7bf8306384e27e8ea8580c6c5')
b2sums=('006fee137176f6fa65acc9cc68f2a1e2f88abd40e6b12b4c530a07c7eea5b98b482bd17eed9bc1fbec9c79abd5b8631fa61fdc7c69e1873d0c477a4f53543b50')
#         '4f7de12ace8af846bafcfe0358f00dd3')
#        '1570ec5fd587860871962d5bf7a2c718b52e6b904a41d084f0df911f289d743bca51d6acc3d7e75f4faebeeb812cf869b2fb2eec20651f6b4ebb854e0935cb36')

#prepare() {
  # Build using system libraries
#  patch -Np1 -i igraph-system-libs20251202.patch
#}

prepare() {
  # Instead of patching, modify files directly with sed

  # 1. In igraph/configure: Remove ${MINI_GMP_SOURCES}
  sed -i "s/OBJECTS='\${IGRAPH_SOURCES} \${GLUE_C_SOURCES} \${GLUE_CPP_SOURCES} \${MINI_GMP_SOURCES}'/OBJECTS='\${IGRAPH_SOURCES} \${GLUE_C_SOURCES} \${GLUE_CPP_SOURCES}'/" igraph/configure

  # 2. In igraph/src/Makevars.in: Add -I/usr/include/uuid to PKG_CPPFLAGS
  sed -i 's|PKG_CPPFLAGS=-DUSING_R -I\. -Ivendor|PKG_CPPFLAGS=-DUSING_R -I/usr/include/uuid -I. -Ivendor|' igraph/src/Makevars.in

  # 3. In igraph/src/Makevars.in: Add -lgmp -luuid to PKG_LIBS
  sed -i 's|PKG_LIBS = @libs@ $(LAPACK_LIBS) $(BLAS_LIBS) $(FLIBS)|PKG_LIBS = @libs@ $(LAPACK_LIBS) $(BLAS_LIBS) $(FLIBS) -lgmp -luuid|' igraph/src/Makevars.in

  # 4. In igraph/src/vendor/config.h: Remove INTERNAL_GMP definition
  sed -i '/^#define INTERNAL_GMP 1$/d' igraph/src/vendor/config.h

  # 5. In igraph/src/vendor/config.h: Fix indentation for HAVE___UINT128_T
  sed -i 's/^#  define HAVE___UINT128_T 1/#define HAVE___UINT128_T 1/' igraph/src/vendor/config.h
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
