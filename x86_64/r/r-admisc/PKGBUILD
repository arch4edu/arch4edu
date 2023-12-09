# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=admisc
_pkgver=0.34
pkgname=r-${_pkgname,,}
pkgver=0.34
pkgrel=1
pkgdesc="Adrian Dusa's Miscellaneous"
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
optdepends=(
  r-qca
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('fdcf875e6440fd049a78171db2594d6d963c484eca9387f852c5c8b3208a5bdf')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
