# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=strucchange
_pkgver=1.5-4
pkgname=r-${_pkgname,,}
pkgver=1.5.4
pkgrel=1
pkgdesc='Testing, Monitoring, and Dating Structural Changes'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-sandwich
  r-zoo
)
optdepends=(
  r-car
  r-dynlm
  r-e1071
  r-foreach
  r-lmtest
  r-mvtnorm
  r-stats4
  r-tseries
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('789bc64d36a79539d17db5e3d50a3f32cf709a42177ffd336c10a8201b5dd718')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
