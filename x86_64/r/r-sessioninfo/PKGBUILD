# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=sessioninfo
_pkgver=1.2.3
pkgname=r-${_pkgname,,}
pkgver=1.2.3
pkgrel=1
pkgdesc='R Session Information'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-cli
)
optdepends=(
  r-callr
  r-covr
  r-mockery
  r-reticulate
  r-rmarkdown
  r-testthat
  r-withr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('a02b90a8a6c49a499d972cebc5a15ab44e729b232d00516cb168414701e1c650')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
