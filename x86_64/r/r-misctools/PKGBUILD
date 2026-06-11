# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=miscTools
_pkgver=0.6-30
pkgname=r-${_pkgname,,}
pkgver=0.6.30
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
sha256sums=('961dd2fb2ad7aeb17082e1ced36776a5574f8a068564cb633127c78347fefd3d')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
