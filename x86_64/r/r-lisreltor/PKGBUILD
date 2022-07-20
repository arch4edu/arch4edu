# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=lisrelToR
_pkgver=0.1.5
pkgname=r-${_pkgname,,}
pkgver=0.1.5
pkgrel=7
pkgdesc="Import Output from 'LISREL' into 'R'"
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('d35981f45f08c82272d2fd58b284c19f60c3492aadbd3781a7e788833ad8a144')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
