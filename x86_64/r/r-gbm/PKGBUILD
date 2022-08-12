# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=gbm
_pkgver=2.1.8.1
pkgname=r-${_pkgname,,}
pkgver=2.1.8.1
pkgrel=1
pkgdesc='Generalized Boosted Regression Models'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
optdepends=(
  r-covr
  r-gridextra
  r-knitr
  r-pdp
  r-runit
  r-splines
  r-tinytest
  r-vip
  r-viridis
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('8d2456124552658ee9500707c4e9992cf42cb88705008c32ea258efb4f2be80b')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
