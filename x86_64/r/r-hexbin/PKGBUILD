# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_cranname=hexbin
_cranver=1.28.2
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="Hexagonal Binning Routines"
arch=(i686 x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(GPL2)
depends=(r)
makedepends=(gcc-fortran)
optdepends=(
    r-marray
    r-affy
    r-biobase
    r-limma
    r-knitr
)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
sha256sums=('6241f8d3a6c6be2c1c693c3ddb99554bc103e3c6cf602d0c2787c0ce6fd1702d')

build() {
  mkdir -p build
  R CMD INSTALL "${_cranname}" -l "${srcdir}/build"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"

  cp -a --no-preserve=ownership "build/${_cranname}" "${pkgdir}/usr/lib/R/library"
}
