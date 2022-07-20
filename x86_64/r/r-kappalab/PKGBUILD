# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=kappalab
_pkgver=0.4-7
pkgname=r-${_pkgname,,}
pkgver=0.4.7
pkgrel=5
pkgdesc='Non-Additive Measure and Integral Manipulation Functions'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('CeCILL')
depends=(
  r
  r-lpsolve
  r-quadprog
  r-kernlab
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('00571c3e2022f65020aec1d3400b46ec390e90078f8f8bfc3e5ce08a395f7c99')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
