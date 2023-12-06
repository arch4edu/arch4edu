# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=sets
_pkgver=1.0-25
pkgname=r-${_pkgname,,}
pkgver=1.0.25
pkgrel=1
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
sha256sums=('5ca469218f9679f2372e33e56f781b52947ccbedf730b91a2d3a572993c024f4')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
