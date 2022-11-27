# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=EnvStats
_pkgver=2.7.0
pkgname=r-${_pkgname,,}
pkgver=2.7.0
pkgrel=6
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
sha256sums=('09a6f0d5b60856c7298371e4a8a085a1db7abf0e71ccb9a2dc9ca24248fb5d81')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
