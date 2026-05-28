# system requirements: GNU make
# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=FrF2
_pkgver=2.3-5
pkgname=r-${_pkgname,,}
pkgver=2.3.5
pkgrel=1
pkgdesc="Fractional Factorial Designs with 2-Level Factors"
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-doe.base
  r-sfsmisc
  r-scatterplot3d
  r-igraph
)
optdepends=(
  r-bsmd
  r-doe.wrapper
  r-frf2.catlg128
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('8bda7afaa1a1dab4da447477d6f5408567e2a0c6e0c93d6ab0bccc16ff7eb9f7')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
