# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=pbapply
_pkgver=1.5-0
pkgname=r-${_pkgname,,}
pkgver=1.5.0
pkgrel=4
pkgdesc="Adding Progress Bar to '*apply' Functions"
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
optdepends=(
  r-shiny
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('effdfee286e5ba9534dc2ac3cee96590a37f5cd2af28c836d00c25ca9f070a55')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
