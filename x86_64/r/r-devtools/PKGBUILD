# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Kibouo <csonka.mihaly@hotmail.com>
# Contributor: Ward Segers <w@rdsegers.be>
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=devtools
_pkgver=2.4.5
pkgname=r-${_pkgname,,}
pkgver=2.4.5
pkgrel=5
pkgdesc='Tools to Make Developing R Packages Easier'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('MIT')
depends=(
  r
  r-cli
  r-desc
  r-ellipsis
  r-fs
  r-lifecycle
  r-memoise
  r-miniui
  r-pkgbuild
  r-pkgdown
  r-pkgload
  r-profvis
  r-rcmdcheck
  r-remotes
  r-rlang
  r-roxygen2
  r-rversions
  r-sessioninfo
  r-testthat
  r-urlchecker
  r-usethis
  r-withr
)
optdepends=(
  r-biocmanager
  r-callr
  r-covr
  r-curl
  r-digest
  r-dt
  r-foghorn
  r-gh
  r-gmailr
  r-httr
  r-knitr
  r-lintr
  r-mass
  r-mockery
  r-pingr
  r-rhub
  r-rmarkdown
  r-rstudioapi
  r-spelling
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('38160ebd839acdec7ebf0699a085b4ab1ebd5500d3c57a9fa7ae484f1909904b')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
  install -Dm644 "${_pkgname}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
