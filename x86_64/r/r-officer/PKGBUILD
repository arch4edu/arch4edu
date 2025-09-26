# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=officer
_pkgver=0.7.0
pkgname=r-${_pkgname,,}
pkgver=0.7.0
pkgrel=1
pkgdesc='Manipulation of Microsoft Word and PowerPoint Documents'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-openssl
  r-r6
  r-ragg
  r-uuid
  r-xml2
  r-zip
)
optdepends=(
  r-devemf
  r-doconv
  r-ggplot2
  r-knitr
  r-magick
  r-rmarkdown
  r-rsvg
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('baf7a7b880d79ef9769b1b3e013a53ec777ee871d9e148d0ec7eb1a19ed6c8a6')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
