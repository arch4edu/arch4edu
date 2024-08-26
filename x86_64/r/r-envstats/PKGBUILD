# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=EnvStats
_pkgver=3.0.0
pkgname=r-${_pkgname,,}
pkgver=3.0.0
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
sha256sums=('0413ec3d44b3251549a254b4afd76f520aaacd5374b463a5813e23e1fa8cd248')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
