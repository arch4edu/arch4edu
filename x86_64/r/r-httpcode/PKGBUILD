# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=httpcode
_pkgver=0.3.0
pkgname=r-${_pkgname,,}
pkgver=0.3.0
pkgrel=4
pkgdesc="'HTTP' Status Code Helper"
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('MIT')
depends=(
  r
)
optdepends=(
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('593a030a4f94c3df8c15576837c17344701bac023ae108783d0f06c476062f76')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
  install -Dm644 "${_pkgname}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
