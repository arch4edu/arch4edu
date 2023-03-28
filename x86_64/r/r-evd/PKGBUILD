# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=evd
_pkgver=2.3-6.1
pkgname=r-${_pkgname,,}
pkgver=2.3.6.1
pkgrel=6
pkgdesc='Functions for Extreme Value Distributions'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
optdepends=(
  r-interp
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('662c592d3f5c5693dbf1c673d1137c4a60a347e330b71be1f3933f201d2c8971')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
