# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=sets
_pkgver=1.0-23
pkgname=r-${_pkgname,,}
pkgver=1.0.23
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
sha256sums=('e5b6bc52060421c572d7f2d99b25909a38eacabd5344a47e1cdb2662c62d690b')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
