# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Maintainer: Robert Greener <me@r0bert.dev>
# Contributor: Hyacinthe Cartiaux <hyacinthe.cartiaux@free.fr>
_pkgname=ggpp
_pkgver=0.5.2
pkgname=r-${_pkgname,,}
pkgver=0.5.2
pkgrel=3
pkgdesc="Grammar Extensions to 'ggplot2'"
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-dplyr
  r-ggplot2
  r-glue
  r-gridextra
  r-lubridate
  r-magrittr
  r-polynom
  r-rlang
  r-scales
  r-stringr
  r-tibble
  r-xts
  r-zoo
)
optdepends=(
  r-gginnards
  r-ggrepel
  r-knitr
  r-magick
  r-rmarkdown
  r-testthat
  r-vdiffr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('b3e25283ab68391bdbe82342d6bd012b00ea9e30099bdc746b30460f8f202371')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
