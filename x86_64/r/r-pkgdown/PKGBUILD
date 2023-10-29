# system requirements: pandoc
# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=pkgdown
_pkgver=2.0.7
pkgname=r-${_pkgname,,}
pkgver=2.0.7
pkgrel=1
pkgdesc='Make Static HTML Documentation for a Package'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('MIT')
depends=(
  r
  r-bslib
  r-callr
  r-cli
  r-desc
  r-digest
  r-downlit
  r-fs
  r-httr
  r-jsonlite
  r-magrittr
  r-memoise
  r-purrr
  r-ragg
  r-rlang
  r-rmarkdown
  r-tibble
  r-whisker
  r-withr
  r-xml2
  r-yaml
)
optdepends=(
  r-covr
  r-diffviewer
  r-evaluate
  r-htmltools
  r-htmlwidgets
  r-knitr
  r-lifecycle
  r-methods
  r-openssl
  r-pkgload
  r-rsconnect
  r-rstudioapi
  r-rticles
  r-sass
  r-testthat
  r-tools
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('f33872869dfa8319182d87e90eab3245ff69293b3b791471bf9538afb81b356a')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
  install -Dm644 "${_pkgname}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
