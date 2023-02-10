# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=kappalab
_pkgver=0.4-10
pkgname=r-${_pkgname,,}
pkgver=0.4.10
pkgrel=1
pkgdesc='Non-Additive Measure and Integral Manipulation Functions'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('CeCILL')
depends=(
  r
  r-lpsolve
  r-quadprog
  r-kernlab
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('e95d98ace59b0bc0b9f0f8beb52ed60264f62c25a637bdc10f6f57f9d474dd93')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
