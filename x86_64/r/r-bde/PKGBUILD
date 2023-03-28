# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=bde
_pkgver=1.0.1.1
pkgname=r-${_pkgname,,}
pkgver=1.0.1.1
pkgrel=1
pkgdesc='Bounded Density Estimation'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-ggplot2
  r-shiny
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('69d9bf5757ee7cf9fe1f5cf4d603570ae1d0b8210968e6ac5dfe7c3cbde6aa45')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
