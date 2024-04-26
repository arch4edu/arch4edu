# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=geometry
_pkgver=0.4.7
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=5
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
md5sums=('3c072c129e57358977b9a59445206b36')
b2sums=('6185f018755f36fca96b6b5de37420f142bd4e65e011b91c2e88c129c4a1bda0100ea8fe5b9b4aa02c3ba223afc71567f37d01676578342d81468b3eb34c0be1')

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
