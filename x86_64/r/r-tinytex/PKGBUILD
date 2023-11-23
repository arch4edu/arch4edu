# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: anzi2001 <anzi2001 at gmail dot com>
# Contributor: haha662 <haha662 at outlook dot com>
# Contributor: Kibouo <csonka.mihaly@hotmail.com>
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=tinytex
_pkgver=0.49
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Helper Functions to Install and Maintain TeX Live, and Compile LaTeX Documents"
arch=(any)
url="https://cran.r-project.org/package=${_pkgname}"
license=(MIT)
depends=(
  r-xfun
)
checkdepends=(
  r-testit
)
optdepends=(
  r-rstudioapi
  r-testit
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('0e44e8589e71a5257ddac72c5113e440')
sha256sums=('941169ec65445d172658d0fb6ea8d839736f3f1b5f6ce20637d7d8e299663145')

build() {
  mkdir -p build
  R CMD INSTALL "$_pkgname" -l build
}

check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" _R_CHECK_PACKAGE_NAME_=false Rscript --vanilla test-cran.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"

  install -d "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "/usr/lib/R/library/$_pkgname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"
}
