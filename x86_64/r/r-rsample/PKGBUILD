# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=rsample
_pkgver=1.1.1
pkgname=r-${_pkgname,,}
pkgver=1.1.1
pkgrel=3
pkgdesc='General Resampling Infrastructure'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('MIT')
depends=(
  r
  r-dplyr
  r-furrr
  r-generics
  r-glue
  r-pillar
  r-purrr
  r-rlang
  r-slider
  r-tibble
  r-tidyr
  r-tidyselect
  r-vctrs
)
optdepends=(
  r-broom
  r-covr
  r-ggplot2
  r-knitr
  r-modeldata
  r-recipes
  r-rmarkdown
  r-stats
  r-testthat
  r-utils
  r-whisker
  r-withr
  r-xml2
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('90d2ae86d27a397ba9d8d010e7dea5c7b86fecbec7e9af273db0c2e8c374b8ba')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
  install -Dm644 "${_pkgname}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
