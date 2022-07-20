# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=combinat
_pkgver=0.0-8
pkgname=r-${_pkgname,,}
pkgver=0.0.8
pkgrel=4
pkgdesc='combinatorics utilities'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('1513cf6b6ed74865bfdd9f8ca58feae12b62f38965d1a32c6130bef810ca30c1')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
