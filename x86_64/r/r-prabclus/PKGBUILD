# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=prabclus
_pkgver=2.3-3
pkgname=r-${_pkgname,,}
pkgver=2.3.3
pkgrel=3
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
  r-mvtnorm
  r-spatialreg
  r-spdep
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('005d000a9ac357e670de26e5b8fc4ddb1617351275fa43bf6d2e88b8774358c1')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
