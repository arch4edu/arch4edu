# system requirements: cairo, freetype2, fontconfig
# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: portaloffreedom

_pkgname=gdtools
_pkgver=0.2.4
pkgname=r-${_pkgname,,}
pkgver=0.2.4
pkgrel=6
pkgdesc='Utilities for Graphical Rendering'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-rcpp
  r-systemfonts
  cairo
  freetype2
  fontconfig
)
optdepends=(
  r-curl
  r-fontquiver
  r-htmltools
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('32884ce1aa49be1fd897b4f808cdbc8727cb0d881ff8961e899220b2cac33028')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
