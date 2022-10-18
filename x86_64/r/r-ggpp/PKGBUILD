# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Maintainer: Robert Greener <me@r0bert.dev>
# Contributor: Hyacinthe Cartiaux <hyacinthe.cartiaux@free.fr>
_pkgname=ggpp
_pkgver=0.4.5
pkgname=r-${_pkgname,,}
pkgver=0.4.5
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
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('e98a9eb121de49c72fa58e5a093f72cadbab0b0be15b80d791ba7ff1dde6360a')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
