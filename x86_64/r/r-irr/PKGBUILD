# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=irr
_pkgver=0.84.1
pkgname=r-${_pkgname,,}
pkgver=0.84.1
pkgrel=4
pkgdesc='Various Coefficients of Interrater Reliability and Agreement'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-lpsolve
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('e7bae8476b723a2246564c013194e8b7fcc9b34affc0ab5fcd55875231f544c3')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
