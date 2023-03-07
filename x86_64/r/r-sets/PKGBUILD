# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=sets
_pkgver=1.0-24
pkgname=r-${_pkgname,,}
pkgver=1.0.24
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
sha256sums=('e75733f5c9418eb09fb950a4a94ccf84ddd88231c61ee80d02b7f0917debcac9')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
