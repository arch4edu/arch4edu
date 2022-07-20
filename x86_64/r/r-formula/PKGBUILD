# Maintainer: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_cranname=Formula
_cranver=1.2-4
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="Extended Model Formulas"
arch=(any)
url="https://cran.r-project.org/package=${_cranname}"
license=(GPL2 GPL3)
depends=('r>=2.0.0')
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
sha256sums=('cb70e373b5ed2fc8450937fb3321d37dfd22dcc6f07cb872a419d51205125caf')

build() {
  R CMD INSTALL ${_cranname}_${_cranver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"

  cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
}
