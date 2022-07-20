# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_cranname=coin
_cranver=1.4-2
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="Conditional Inference Procedures in a Permutation Test Framework"
arch=(i686 x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(GPL2)
depends=('r>=3.6.0' 'r-libcoin>=1.0.9' 'r-matrixstats>=0.54.0' 'r-modeltools>=0.2.9' 'r-mvtnorm>=1.0.5' r-multcomp)
optdepends=(r-xtable r-e1071 r-vcd r-th.data)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
sha256sums=('7546d1f27a82d98b4b3e43e4659eba0f74a67d5919ce85d2fb360282ba3cfbb2')

build() {
  R CMD INSTALL ${_cranname}_${_cranver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"

  cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
}
