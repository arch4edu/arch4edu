# system requirements: TensorFlow (https://www.tensorflow.org/)
# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=tfautograph
_pkgver=0.3.2
pkgname=r-${_pkgname,,}
pkgver=0.3.2
pkgrel=4
pkgdesc="Autograph R for 'Tensorflow'"
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-backports
  r-reticulate
)
optdepends=(
  r-rlang
  r-tensorflow
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('42821583679d32fa4abb4304b6831e8c3b4dce9468e1a3b570af7bf95ec0aa3a')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
