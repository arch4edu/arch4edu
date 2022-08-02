# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=NetworkComparisonTest
_pkgver=2.2.1
pkgname=r-${_pkgname,,}
pkgver=2.2.1
pkgrel=1
pkgdesc='Statistical Comparison of Two Networks Based on Three Invariance Measures'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-isingfit
  r-isingsampler
  r-qgraph
  r-reshape2
)
optdepends=(
  r-networktools
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('1753961e9fb41d3aae6d12392445d7468d312a5e42629d34597ffa1e6e329b28')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
