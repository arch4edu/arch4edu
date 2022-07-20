# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Grey Christoforo <first name at last name dot net>

_cranname=colorspace
_cranver=2.0-3
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="A Toolbox for Manipulating and Assessing Colors and Palettes"
arch=(i686 x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(BSD3)
depends=('r>=3.0.0')
optdepends=(r-kernlab r-mvtnorm r-vcd r-shiny r-shinyjs r-ggplot2 r-dplyr r-scales r-png r-jpeg r-knitr r-rmarkdown r-rcolorbrewer r-rcartocolor r-scico r-viridis r-wesanderson)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
sha256sums=('e75681cc4dd6e4b70303fd96a6d4597065dc6bffcaa4ae4244b73ff19016857f')

build() {
  R CMD INSTALL ${_cranname}_${_cranver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"

  cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
}
