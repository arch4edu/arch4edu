# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=VGAM
_pkgver=1.1-9
pkgname=r-${_pkgname,,}
pkgver=1.1.9
pkgrel=1
pkgdesc='Vector Generalized Linear and Additive Models'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
optdepends=(
  r-mass
  r-mgcv
  r-vgamdata
  r-vgamextra
)
makedepends=(
  gcc-fortran
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('d4d411b020acaec32777c89e2b2265449e6855794442b2c4c51bcd9288b1afd0')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
