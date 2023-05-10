# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=rvg
_pkgver=0.3.3
pkgname=r-${_pkgname,,}
pkgver=0.3.3
pkgrel=1
pkgdesc='R Graphics Devices for Vector Graphics Output'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-gdtools
  r-officer
  r-rcpp
  r-rlang
  r-xml2
)
optdepends=(
  r-grid
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('15c8157ae2383c9452988b31420648be5bc8b4d0e5181be66c65e73262743d55')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
