# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_cranname=miniUI
_cranver=0.1.1.1
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="Shiny UI Widgets for Small Screens"
arch=(any)
url="https://cran.r-project.org/package=${_cranname}"
license=(GPL3)
depends=(r 'r-shiny>=0.13' 'r-htmltools>=0.3')
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
sha256sums=('452b41133289f630d8026507263744e385908ca025e9a7976925c1539816b0c0')

build() {
  R CMD INSTALL ${_cranname}_${_cranver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"

  cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
}
