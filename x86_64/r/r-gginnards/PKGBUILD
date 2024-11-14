# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=gginnards
_pkgver=0.2.0-1
pkgname=r-${_pkgname,,}
pkgver=0.2.0.1
pkgrel=1
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
sha256sums=('83a66db01d94f50004a188db35da274eb9ffda737f1eff11e57bbd8b306c5d18')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
