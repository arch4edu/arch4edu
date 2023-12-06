# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=AcceptanceSampling
_pkgver=1.0-10
pkgname=r-${_pkgname,,}
pkgver=1.0.10
pkgrel=1
pkgdesc='Creation and Evaluation of Acceptance Sampling Plans'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('c574f742d1a9c2ea6153aff54a6dcae6694ab7f895ca8d6b7b1f58bbb3177be9')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
