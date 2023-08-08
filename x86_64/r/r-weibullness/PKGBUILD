# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=weibullness
_pkgver=1.23.8
pkgname=r-${_pkgname,,}
pkgver=1.23.8
pkgrel=1
pkgdesc='Goodness-of-Fit Test for Weibull Distribution (Weibullness)'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('a4900ba049ac0e575f4e634ea0464e011c93cb4138970bff058120f9eb4c381e')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
