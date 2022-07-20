# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=corpcor
_pkgver=1.6.10
pkgname=r-${_pkgname,,}
pkgver=1.6.10
pkgrel=4
pkgdesc='Efficient Estimation of Covariance and (Partial) Correlation'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('71a04c503c93ec95ddde09abe8c7ddeb36175b7da76365a14b27066383e10e09')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
