# system requirements: pandoc
# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=pkgdown
_pkgver=2.1.1
pkgname=r-${_pkgname,,}
pkgver=2.1.1
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
  r-fontawesome
  r-fs
  r-httr2
  r-jsonlite
  r-openssl
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
  r-gert
  r-gt
  r-htmltools
  r-htmlwidgets
  r-knitr
  r-lifecycle
  r-magick
  r-methods
  r-pkgload
  r-quarto
  r-rsconnect
  r-rstudioapi
  r-rticles
  r-sass
  r-testthat
  r-tools
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('c7e1c374f8c4684da630cbb471793ae36396beb92318620230159da0026c0cde')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
  install -Dm644 "${_pkgname}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
