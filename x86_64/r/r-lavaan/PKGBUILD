# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=lavaan
_pkgver=0.6-13
pkgname=r-${_pkgname,,}
pkgver=0.6.13
pkgrel=1
pkgdesc='Latent Variable Analysis'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-mnormt
  r-numderiv
  r-pbivnorm
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('2af8428e3679ed9889f353015135500ba2b88bd44b5b74f7eea37ff442558c3e')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
