# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=prabclus
_pkgver=2.3-2
pkgname=r-${_pkgname,,}
pkgver=2.3.2
pkgrel=4
pkgdesc='Functions for Clustering and Testing of Presence-Absence, Abundance and Multilocus Genetic Data'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-mclust
)
optdepends=(
  r-bootstrap
  r-foreign
  r-maptools
  r-mvtnorm
  r-spatialreg
  r-spdep
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('f421bcbcb557281e0de4a06b15f9a496adb5c640e883c0f7bb12051efc69e441')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
