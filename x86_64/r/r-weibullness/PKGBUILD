# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=weibullness
_pkgver=1.19.8
pkgname=r-${_pkgname,,}
pkgver=1.19.8
pkgrel=5
pkgdesc='Goodness-of-Fit Test for Weibull Distribution (Weibullness)'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('b9a6296e68d18fd37a2b7e3d5cb9e76bffa446965e43dd5d7c165ad67b2544a7')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
