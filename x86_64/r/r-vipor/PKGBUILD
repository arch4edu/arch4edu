# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=vipor
_pkgver=0.4.7
pkgname=r-${_pkgname,,}
pkgver=0.4.7
pkgrel=1
pkgdesc='Plot Categorical Data Using Quasirandom Noise and Density Estimates'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
optdepends=(
  r-beanplot
  r-beeswarm
  r-ggbeeswarm
  r-ggplot2
  r-lattice
  r-testthat
  r-vioplot
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('baad41e9ddaa13b5a1db1abab34253b27d5b99e5a6a649b2036aaf1483370b9e')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
