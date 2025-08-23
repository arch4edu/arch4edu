# system requirements: TensorFlow (https://www.tensorflow.org/)
# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=tensorflow
_pkgver=2.20.0
pkgname=r-${_pkgname,,}
pkgver=2.20.0
pkgrel=1
pkgdesc="R Interface to 'TensorFlow'"
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('Apache')
depends=(
  r
  r-config
  r-lifecycle
  r-processx
  r-reticulate
  r-rstudioapi
  r-tfautograph
  r-tfruns
  r-yaml
)
optdepends=(
  r-callr
  r-keras
  r-pillar
  r-testthat
  r-withr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('e63a87c5077bfbd1aa1f6d276dc625f30c4662ebd36d86726c30d2d5749b31c1')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
