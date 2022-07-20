# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=moments
_pkgver=0.14.1
pkgname=r-${_pkgname,,}
pkgver=0.14.1
pkgrel=1
pkgdesc='Moments, cumulants, skewness, kurtosis and related tests'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('2ed2b84802da132ae0cf826a65de5bfa85042b82e086be844002fe1ce270d864')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
