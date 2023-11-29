# system requirements: gmp (>= 4.2.3)
# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=gmp
_pkgver=0.7-3
pkgname=r-${_pkgname,,}
pkgver=0.7.3
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
sha256sums=('606d0f7fbbf81ad61dcfa5e83002fc274a5ebf6b4ff5c9a9b69f141f886ac665')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
