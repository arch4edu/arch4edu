# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=gnm
_pkgver=1.1-3
pkgname=r-${_pkgname,,}
pkgver=1.1.3
pkgrel=1
pkgdesc='Generalized Nonlinear Models'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-qvcalc
  r-relimp
)
optdepends=(
  r-testthat
  r-vcdextra
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('d22962963545b3aa1de3a563c5ae4b8038b09c7a9a96185708b35c4d032b1c37')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
