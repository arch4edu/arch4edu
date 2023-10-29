# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=alabama
_pkgver=2023.1.0
pkgname=r-${_pkgname,,}
pkgver=2023.1.0
pkgrel=1
pkgdesc='Constrained Nonlinear Optimization'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-numderiv
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('925f67c72d9cdb677105377777bd09e9b56a61573bea7e3f69e0a49595c7bf1c')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
