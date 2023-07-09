# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=EnvStats
_pkgver=2.8.0
pkgname=r-${_pkgname,,}
pkgver=2.8.0
pkgrel=1
pkgdesc='Package for Environmental Statistics, Including US EPA Guidance'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-ggplot2
  r-nortest
)
optdepends=(
  r-boot
  r-covr
  r-hmisc
  r-lattice
  r-qcc
  r-sp
  r-tinytest
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('b7a048a298418521df7bebef22fc0ea0d675e74244865bd2ecfaca968be2cf9d')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
