# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=modules
_pkgver=0.11.0
pkgname=r-${_pkgname,,}
pkgver=0.11.0
pkgrel=1
pkgdesc='Self Contained Units of Source Code'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('MIT')
depends=(
  r
)
optdepends=(
  r-devtools
  r-knitr
  r-lintr
  r-parallel
  r-rmarkdown
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('77c3c18e4a81d6f53dbc16d09a4c6634eff0ec301e36f1b398585ce666824cf8')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
  install -Dm644 "${_pkgname}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
