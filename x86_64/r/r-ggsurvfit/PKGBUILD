# Maintainer: Shun Wang <shuonwang at gmail dot com>

_pkgname=ggsurvfit
_pkgver=1.2.0
pkgname=r-${_pkgname,,}
pkgver=1.2.0
pkgrel=1
pkgdesc='Flexible Time-to-Event Figures'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('MIT')
depends=(
  r
  r-broom
  r-cli
  r-dplyr
  r-ggplot2
  r-glue
  r-gtable
  r-patchwork
  r-tidyr
)
optdepends=(
  r-covr
  r-knitr
  r-rmarkdown
  r-scales
  r-spelling
  r-testthat
  r-tidycmprsk
  r-vdiffr
  r-withr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('99d2381eab75699450d6fe2fe134ce33f581bb87b4e6bb58ce375b8d0d9d2e36')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
