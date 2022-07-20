# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_cranname=statmod
_cranver=1.4.36
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="Statistical Modeling"
arch=(i686 x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(GPL2 GPL3)
depends=('r>=3.0.0' gcc-fortran)
makedepends=(gcc-fortran)
optdepends=(r-tweedie)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
sha256sums=('14e897c83d426caca4d920d3d5bead7ae9a679276b3cb2e227f299ad189d7bc2')

build() {
  R CMD INSTALL ${_cranname}_${_cranver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"

  cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
}
