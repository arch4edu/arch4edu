# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=gplots
_pkgver=3.1.3
pkgname=r-${_pkgname,,}
pkgver=3.1.3
pkgrel=1
pkgdesc='Various R Programming Tools for Plotting Data'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-catools
  r-gtools
)
optdepends=(
  r-grid
  r-knitr
  r-mass
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('9f853b9e205264d087e61e8825f797ce36c9eb585b187dab794563613a526716')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
