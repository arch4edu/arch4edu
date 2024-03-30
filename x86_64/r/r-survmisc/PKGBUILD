# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=survMisc
_pkgver=0.5.6
pkgname=r-${_pkgname,,}
pkgver=0.5.6
pkgrel=3
pkgdesc='Miscellaneous Functions for Survival Data'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-data.table
  r-ggplot2
  r-gridextra
  r-km.ci
  r-kmsurv
  r-knitr
  r-xtable
  r-zoo
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('d911125bc374dfc67f31a81ebeaf98a09cac8f81e30259655ab136ebf4718c04')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
