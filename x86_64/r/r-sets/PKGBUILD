# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=sets
_pkgver=1.0-21
pkgname=r-${_pkgname,,}
pkgver=1.0.21
pkgrel=4
pkgdesc='Sets, Generalized Sets, Customizable Sets and Intervals'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
optdepends=(
  r-proxy
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('5733f0be59189c058c069583f5c4dc1d772bfad5abbfd16081131414d6002ac0')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
