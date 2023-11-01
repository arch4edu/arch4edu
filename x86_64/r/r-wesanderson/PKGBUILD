# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=wesanderson
_pkgver=0.3.7
pkgname=r-${_pkgname,,}
pkgver=0.3.7
pkgrel=1
pkgdesc='A Wes Anderson Palette Generator'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('MIT')
depends=(
  r
)
optdepends=(
  r-ggplot2
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('c92e5604e1e149e00f49fd236c6ab8cd09d96106eb14479f7839e6996bf95e4e')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
  install -Dm644 "${_pkgname}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
