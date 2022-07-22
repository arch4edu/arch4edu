# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=IsingSampler
_pkgver=0.2.1
pkgname=r-${_pkgname,,}
pkgver=0.2.1
pkgrel=4
pkgdesc='Sampling Methods and Distribution Functions for the Ising Model'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-dplyr
  r-magrittr
  r-plyr
  r-rcpp
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('fb9d1c851941d74d218ae5be6d45ea3e9c228c938ef9cdfd34de9535cadc44b3')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
