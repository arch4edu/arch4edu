# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=lifecycle
_pkgver=1.0.2
pkgname=r-${_pkgname,,}
pkgver=1.0.2
pkgrel=1
pkgdesc='Manage the Life Cycle of your Package Functions'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('MIT')
depends=(
  r
  r-glue
  r-rlang
)
optdepends=(
  r-covr
  r-crayon
  r-knitr
  r-lintr
  r-rmarkdown
  r-testthat
  r-tibble
  r-tidyverse
  r-tools
  r-vctrs
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('7b3f3c8ef9c068c5db396b353d62185d9ed02a69b787c7769d24595769a25a63')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
  install -Dm644 "${_pkgname}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
