# system requirements: GNU make
# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=FrF2
_pkgver=2.3-3
pkgname=r-${_pkgname,,}
pkgver=2.3.3
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
sha256sums=('bd77912e478adece8b9aa31c17e1f9683e4f2e098d6f183fd34e15ab3a7e9286')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
