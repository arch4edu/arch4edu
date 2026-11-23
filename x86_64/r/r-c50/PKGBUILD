# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=C50
_pkgver=1.0.1
pkgname=r-${_pkgname,,}
pkgver=1.0.1
pkgrel=1
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
sha256sums=('79596d8fa98f561fd181d92129ec582ca7890b29a875000ff45e7c61fe2c265e')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
