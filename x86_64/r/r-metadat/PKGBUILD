# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=metadat
_pkgver=1.2-0
pkgname=r-${_pkgname,,}
pkgver=1.2.0
pkgrel=1
pkgdesc='Meta-Analysis Datasets'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-mathjaxr
)
optdepends=(
  r-ape
  r-biasedurn
  r-clubsandwich
  r-dfoptim
  r-digest
  r-gridextra
  r-igraph
  r-lme4
  r-meta
  r-metafor
  r-mvtnorm
  r-netmeta
  r-numderiv
  r-rms
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('f0cce5e30c3d256eaf5a41e4f52ffc7108e195016a4b99409e0ab4c2ef58f5b8')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
