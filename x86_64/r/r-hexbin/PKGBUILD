# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_cranname=hexbin
_cranver=1.28.3
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
sha256sums=('0eb33511c1a4ff29dda8b89fee420ea7041033f981c7f16484c9f504d749de5f')

build() {
  mkdir -p build
  R CMD INSTALL "${_cranname}" -l "${srcdir}/build"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"

  cp -a --no-preserve=ownership "build/${_cranname}" "${pkgdir}/usr/lib/R/library"
}
