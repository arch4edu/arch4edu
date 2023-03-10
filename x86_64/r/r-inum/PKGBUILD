# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=inum
_pkgver=1.0-5
pkgname=r-${_pkgname,,}
pkgver=1.0.5
pkgrel=1
pkgdesc='Interval and Enum-Type Representation of Vectors'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-libcoin
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('e696b7e0b31b3bbf405112e60691b6a72fedcaa02e08ee517c59f6bf9cd36bbd')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
