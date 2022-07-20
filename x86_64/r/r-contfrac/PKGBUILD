# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=contfrac
_pkgver=1.1-12
pkgname=r-${_pkgname,,}
pkgver=1.1.12
pkgrel=5
pkgdesc='Continued Fractions'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('95bfc5e970513416c080486a1cd8dfd9f8d59fb691b02ef6ccbe0ce1ed61056b')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
