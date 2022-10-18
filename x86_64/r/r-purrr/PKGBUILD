# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: frichtlm <frichtlm@gmail.com>

_pkgname=purrr
_pkgver=0.3.5
pkgname=r-${_pkgname,,}
pkgver=0.3.5
pkgrel=3
pkgdesc='Functional Programming Tools'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-magrittr
  r-rlang
)
optdepends=(
  r-covr
  r-crayon
  r-dplyr
  r-knitr
  r-rmarkdown
  r-testthat
  r-tibble
  r-tidyselect
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('a2386cd7e78a043cb9c14703023fff15ab1c879bf648816879d2c0c4a554fcef')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
