# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=statnet.common
_pkgver=4.9.0
pkgname=r-${_pkgname,,}
pkgver=4.9.0
pkgrel=3
pkgdesc='Common R Scripts and Utilities Used by the Statnet Project Software'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-coda
)
optdepends=(
  r-covr
  r-mass
  r-matrix
  r-rlang
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('a485dc6e363a993d87336fbd1027adb1cd7b9103447fd63904cae4dc3bfc2dd7')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
