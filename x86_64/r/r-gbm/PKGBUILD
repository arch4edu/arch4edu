# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=gbm
_pkgver=2.1.8
pkgname=r-${_pkgname,,}
pkgver=2.1.8
pkgrel=4
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
sha256sums=('7d5de3b980b8f23275e86ac9bed48a497c9aa53c58e407dfd676309f38272ec1')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
