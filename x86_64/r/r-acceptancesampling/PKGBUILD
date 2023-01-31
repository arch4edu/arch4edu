# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=AcceptanceSampling
_pkgver=1.0-8
pkgname=r-${_pkgname,,}
pkgver=1.0.8
pkgrel=1
pkgdesc='Creation and Evaluation of Acceptance Sampling Plans'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('5784fa82f3287ef5d57ed294334e61974f77a261fc8c1e90f4c76d8c367841c9')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
