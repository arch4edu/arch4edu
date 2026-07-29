# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=vcd
_pkgver=1.4-14
pkgname=r-${_pkgname,,}
pkgver=1.4.14
pkgrel=1
pkgdesc='Visualizing Categorical Data'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-colorspace
  r-lmtest
)
optdepends=(
  r-coin
  r-hsaur3
  r-kernlab
  r-kernsmooth
  r-mvtnorm
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('7257bea5f4c13b3a0b427149e61f5c40c69050b22a4f9dd1ed5af9d4c3abd13c')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
