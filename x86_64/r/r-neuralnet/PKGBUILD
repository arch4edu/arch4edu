# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=neuralnet
_pkgver=1.44.2
pkgname=r-${_pkgname,,}
pkgver=1.44.2
pkgrel=5
pkgdesc='Training of Neural Networks'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-deriv
)
optdepends=(
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('5f66cd255db633322c0bd158b9320cac5ceff2d56f93e4864a0540f936028826')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
