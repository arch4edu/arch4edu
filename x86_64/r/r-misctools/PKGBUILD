# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=miscTools
_pkgver=0.6-28
pkgname=r-${_pkgname,,}
pkgver=0.6.28
pkgrel=1
pkgdesc='Miscellaneous Tools and Utilities'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-digest
)
optdepends=(
  r-ecdat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('bd4c2f2120948af538f9874df1ac745ff162817d0e53756f52f863eb4f593b21')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
