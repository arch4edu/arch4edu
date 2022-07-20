# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Alex Branham <branham@utexas.edu>

_cranname=foreach
_cranver=1.5.2
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="Provides Foreach Looping Construct"
arch=(any)
url="https://cran.r-project.org/package=${_cranname}"
license=(Apache)
depends=(r-iterators)
checkdepends=(r-doparallel r-testthat)
optdepends=(
    r-randomforest
    r-domc
    r-doparallel
    r-testthat
    r-knitr
    r-rmarkdown
)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
sha256sums=('56338d8753f9f68f262cf532fd8a6d0fe25a71a2ff0107f3ce378feb926bafe4')

build() {
  mkdir -p build
  R CMD INSTALL "${_cranname}" -l "${srcdir}/build"
}

check() {
  cd "${_cranname}/tests"
  R_LIBS="${srcdir}/build" NOT_CRAN=true Rscript --vanilla testthat.R
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"

  cp -a --no-preserve=ownership "build/${_cranname}" "${pkgdir}/usr/lib/R/library"
}
