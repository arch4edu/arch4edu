# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_cranname=fontquiver
_cranver=0.2.1
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="Set of Installed Fonts"
arch=(any)
url="https://cran.r-project.org/package=${_cranname}"
license=(GPL3)
depends=(r-fontbitstreamvera r-fontliberation)
checkdepends=(r-htmltools r-testthat)
optdepends=(r-testthat r-htmltools)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
sha256sums=('95871814c2d55c03ee15a54e29aadfb840c791e1430f94127d9e1dc8608a6363')

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
