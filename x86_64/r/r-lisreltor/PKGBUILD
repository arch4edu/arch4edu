# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=lisrelToR
_pkgver=0.3
pkgname=r-${_pkgname,,}
pkgver=0.3
pkgrel=1
pkgdesc="Import Output from 'LISREL' into 'R'"
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('6bbebbdd6f78ae5d503a4d53558c709233e6e94fe8206f62d5edca3d5b41b4a7')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
