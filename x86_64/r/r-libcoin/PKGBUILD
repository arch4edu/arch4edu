# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_cranname=libcoin
_cranver=1.0-9
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="Linear Test Statistics for Permutation Inference"
arch=(i686 x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(GPL2)
depends=('r>=3.4.0' r-mvtnorm)
optdepends=(r-coin)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
sha256sums=('2d7dd0b7c6dfc20472430570419ea36a714da7bbafd336da1fb53c5c6463d9eb')

build() {
  R CMD INSTALL ${_cranname}_${_cranver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"

  cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
}
