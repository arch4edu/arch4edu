# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_cranname=doParallel
_cranver=1.0.17
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=2
pkgdesc="Foreach Parallel Adaptor for the 'parallel' Package"
arch=(any)
url="https://cran.r-project.org/package=${_cranname}"
license=(GPL2)
depends=(r-foreach r-iterators)
checkdepends=(r-caret r-mlbench r-runit)
optdepends=(r-caret r-mlbench r-runit)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
sha256sums=('b96a25ad105a654d70c7b4ca27290dc9967bc47f4668b2763927a886b178abd7')

build() {
  mkdir -p build
  R CMD INSTALL "${_cranname}" -l "${srcdir}/build"
}

check() {
  cd "${_cranname}/tests"
  R_LIBS="${srcdir}/build" Rscript --vanilla doRUnit.R
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"

  cp -a --no-preserve=ownership "build/${_cranname}" "${pkgdir}/usr/lib/R/library"
}
