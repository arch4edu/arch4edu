# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=alabama
_pkgver=2022.4-1
pkgname=r-${_pkgname,,}
pkgver=2022.4.1
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
sha256sums=('a8c62859b39a8340ecf7bbf411fac303c059e4237d28ff7bba9ba3daaca1d36c')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
