# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=rvg
_pkgver=0.2.5
pkgname=r-${_pkgname,,}
pkgver=0.2.5
pkgrel=5
pkgdesc='R Graphics Devices for Vector Graphics Output'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-gdtools
  r-officer
  r-rcpp
  r-rlang
  r-xml2
)
optdepends=(
  r-covr
  r-grid
  r-htmltools
  r-knitr
  r-rmarkdown
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('92a464c7d4258c7ed20fa315fd392f48e3f870f958edaff923854295b2a60ac4')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
