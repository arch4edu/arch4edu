# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=EnvStats
_pkgver=3.1.0
pkgname=r-${_pkgname,,}
pkgver=3.1.0
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
sha256sums=('c743b833242193d8893d1d6d0d45af091e3c12354e6ab44a787530e83858cd02')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
