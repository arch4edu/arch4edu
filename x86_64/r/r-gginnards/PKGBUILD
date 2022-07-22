# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=gginnards
_pkgver=0.1.0-1
pkgname=r-${_pkgname,,}
pkgver=0.1.0.1
pkgrel=4
pkgdesc="Explore the Innards of 'ggplot2' Objects"
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-ggplot2
  r-magrittr
  r-rlang
  r-stringr
  r-tibble
)
optdepends=(
  r-knitr
  r-pryr
  r-rmarkdown
  r-sf
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('5d0a37295b3b2b067daeca4d9334753e9692fa52872ddca09a58f959b5cefecd')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
