# system requirements: gmp (>= 4.2.3)
# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=gmp
_pkgver=0.6-8
pkgname=r-${_pkgname,,}
pkgver=0.6.8
pkgrel=1
pkgdesc='Multiple Precision Arithmetic'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  gmp
)
optdepends=(
  r-mass
  r-rmpfr
  r-round
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('8e31d5fafac05cc366f6e327f70c3f9f95dccee3c6c7ab05178b39241c406a39')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
