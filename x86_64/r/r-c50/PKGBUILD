# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=C50
_pkgver=0.1.8
pkgname=r-${_pkgname,,}
pkgver=0.1.8
pkgrel=3
pkgdesc='C5.0 Decision Trees and Rule-Based Models'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-cubist
  r-partykit
)
optdepends=(
  r-covr
  r-knitr
  r-modeldata
  r-rmarkdown
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('bbd1bd5ed0ed5257529396697bea2a5841c8159470ba09d2066411d4aeda9c15')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
