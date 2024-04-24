# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=labelled
_pkgver=2.13.0
pkgname=r-${_pkgname,,}
pkgver=2.13.0
pkgrel=1
pkgdesc='Manipulating Labelled Data'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-dplyr
  r-haven
  r-lifecycle
  r-rlang
  r-stringr
  r-tidyr
  r-vctrs
)
optdepends=(
  r-covr
  r-knitr
  r-memisc
  r-questionr
  r-rmarkdown
  r-snakecase
  r-spelling
  r-testthat
  r-utf8
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('9e2e82a42343b62f8a476d4dd7b13e9ffb3ee2c4e23bdf2cd29ef25b3dffa237')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
