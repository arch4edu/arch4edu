# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: frichtlm <frichtlm@gmail.com>

_pkgname=lifecycle
_pkgver=1.0.3
pkgname=r-${_pkgname,,}
pkgver=1.0.3
pkgrel=3
pkgdesc='Manage the Life Cycle of your Package Functions'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('MIT')
depends=(
  r
  r-cli
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
sha256sums=('6459fdc3211585c0cdf120427579c12149b02161efe273a64b825c05e9aa69c2')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
  install -Dm644 "${_pkgname}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
