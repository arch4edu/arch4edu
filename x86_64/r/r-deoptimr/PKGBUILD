# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Alex Branham <branham@utexas.edu>

_cranname=DEoptimR
_cranver=1.0-11
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="Differential Evolution Optimization in Pure R"
arch=(any)
url="https://cran.r-project.org/package=${_cranname}"
license=(GPL)
depends=(r)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
sha256sums=('1874b30f4b75f9bfa891986598f1ebe1fce27fdced14f8f417d3535cac08165b')

build() {
  mkdir -p build
  R CMD INSTALL "${_cranname}" -l "${srcdir}/build"
}

check() {
  cd "${_cranname}/tests"
  R_LIBS="${srcdir}/build" R_PKG_CHECKING_doExtras=true Rscript --vanilla JDEoptim-tst.R
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"

  cp -a --no-preserve=ownership "build/${_cranname}" "${pkgdir}/usr/lib/R/library"
}
