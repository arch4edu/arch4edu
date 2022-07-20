# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Alex Branham <branham@utexas.edu>

_cranname=inline
_cranver=0.3.19
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="Functions to Inline C, C++, Fortran Function Calls from R"
arch=(any)
url="https://cran.r-project.org/package=${_cranname}"
license=(LGPL2 LGPL2.1 LGPL3)
depends=(r)
optdepends=(r-rcpp r-tinytest)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
sha256sums=('0ee9309bb7dab0b97761ddd18381aa12bd7d54678ccd7bec00784e831f4c99d5')

build() {
  R CMD INSTALL ${_cranname}_${_cranver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"

  cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
}
