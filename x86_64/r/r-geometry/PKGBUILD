# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=geometry
_pkgver=0.5.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Mesh Generation and Surface Tessellation"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-or-later')
depends=(
  qhull
  r-linprog
  r-lpsolve
  r-magic
  r-rcpp
)
makedepends=(
  r-rcppprogress
)
checkdepends=(
  r-testthat
)
optdepends=(
  r-interp
  r-r.matlab
  r-rgl
  r-spelling
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('b6036e184b8506546f09f240d2039b22')
b2sums=('82347a9706ed7acfccbcffa713ff40bcc94c475d13738516a720b2b1b27f989c7dd3f0bfbdf833027c9bf1604cb0e9fd0e0bfe4374aa337e27b628ba35d289e8')

prepare() {
  cd "$_pkgname/src"

  # Build against system qhull
  rm *_r.c *_r.h qhull_ra.h
  echo -e 'PKG_LIBS = -lqhull_r\nPKG_CPPFLAGS = -I/usr/include/libqhull_r' >> Makevars

  # Skip test that fails with system qhull
  cd ../tests/testthat
  sed -i '/"convhulln throws an error with duplicated points"/a\ \ skip("Using system qhull")' \
      test-convhulln.R
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
