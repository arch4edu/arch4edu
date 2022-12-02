# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=weibullness
_pkgver=1.22.12
pkgname=r-${_pkgname,,}
pkgver=1.22.12
pkgrel=1
pkgdesc='Goodness-of-Fit Test for Weibull Distribution (Weibullness)'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('9dff63268234fdd4d0b9dfdcdae10fe058a298bfcd98086fb9a7b7456f8b7af6')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
