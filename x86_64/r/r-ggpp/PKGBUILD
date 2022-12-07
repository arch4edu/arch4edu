# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Maintainer: Robert Greener <me@r0bert.dev>
# Contributor: Hyacinthe Cartiaux <hyacinthe.cartiaux@free.fr>
_pkgname=ggpp
_pkgver=0.5.0
pkgname=r-${_pkgname,,}
pkgver=0.5.0
pkgrel=1
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
sha256sums=('e750811c82ac878e084298ea198c48c5454e959df1b9e8ced969f3daf4b7bd7e')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
