# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=R.matlab
_pkgver=3.7.0
pkgname=r-${_pkgname,,}
pkgver=3.7.0
pkgrel=1
pkgdesc='Read and Write MAT Files and Call MATLAB from Within R'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('LGPL')
depends=(
  r
  r-r.methodss3
  r-r.oo
  r-r.utils
)
optdepends=(
  r-matrix
  r-sparsem
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('d713522268a1206555610938350137ea022e07e27fa9cdd73c02fae8d1a43dda')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
