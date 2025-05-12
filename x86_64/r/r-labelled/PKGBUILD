# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=labelled
_pkgver=2.14.1
pkgname=r-${_pkgname,,}
pkgver=2.14.1
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
sha256sums=('8c53ba12c93c3a9a46514eb41c00574fd9be2a98ca716e72ace5a6e3e94eb106')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
