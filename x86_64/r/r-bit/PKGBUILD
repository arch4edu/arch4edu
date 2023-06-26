# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Alex Branham <branham@utexas.edu>

_cranname=bit
_cranver=4.0.5
pkgname=r-${_cranname,,}
pkgver=${_cranver//-/.}
pkgrel=1
pkgdesc="Classes and Methods for Fast Memory-Efficient Boolean Selections"
arch=(i686 x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(GPL)
depends=(r)
optdepends=(
  r-bit64
  r-ff
  r-knitr
  r-microbenchmark
  r-rmarkdown
  r-roxygen2
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
sha256sums=('f0f2536a8874b6a30b80baefbc68cb21f0ffbf51f3877bda8038c3f9f354bfbc')

build() {
  R CMD INSTALL ${_cranname}_${_cranver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"

  cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
}
