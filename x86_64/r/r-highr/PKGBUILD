# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Kibouo <csonka.mihaly@hotmail.com>
# Contributor: Alex Branham <branham@utexas.edu>

_cranname=highr
_cranver=0.10
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="Syntax Highlighting for R Source Code"
arch=(any)
url="https://cran.r-project.org/package=${_cranname}"
license=(GPL)
depends=(r-xfun)
checkdepends=(r-testit)
optdepends=(r-knitr r-markdown r-testit)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
sha256sums=('ec55bc1ff66390ed66806dc2a7b6c17dbfd089b3d73fe2e369017f8cb4bc347b')

build() {
  mkdir -p build
  R CMD INSTALL "${_cranname}" -l "${srcdir}/build"
}

check() {
  cd "${_cranname}/tests"
  R_LIBS="${srcdir}/build" _R_CHECK_PACKAGE_NAME_=false Rscript --vanilla test-all.R
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"

  cp -a --no-preserve=ownership "build/${_cranname}" "${pkgdir}/usr/lib/R/library"
}
