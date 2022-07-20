# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=Rcsdp
_pkgver=0.1.57.2
pkgname=r-${_pkgname,,}
pkgver=0.1.57.2
pkgrel=7
pkgdesc='R Interface to the CSDP Semidefinite Programming Library'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('CPL')
depends=(
  r
)
optdepends=(
  r-matrix
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('a70a84d33750a148657d5f91b181e228311da435e55ab00340e8b41a29c5321f')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
