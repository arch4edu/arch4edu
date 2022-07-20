# Maintainer: Robert Greener <me@r0bert.dev>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_cranname=DT
_cranver=0.23
_updatedate=2022-06-08
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="A Wrapper of the JavaScript Library 'DataTables'"
arch=(any)
url="https://cran.r-project.org/package=${_cranname}"
license=(GPL3)
depends=(r 'r-htmltools>=0.3.6' 'r-htmlwidgets>=1.3' 'r-jsonlite>=0.9.16' r-magrittr r-crosstalk r-jquerylib r-promises)
optdepends=(r-knitr r-rmarkdown r-shiny r-bslib r-testit)
source=("https://cran.microsoft.com/snapshot/${_updatedate}/src/contrib/${_cranname}_${_cranver}.tar.gz")
sha256sums=('360ae2fcb1141125a1b16448570fc37d14c4dd3f78a872c26df4fda1787cdc70')

build() {
  R CMD INSTALL ${_cranname}_${_cranver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"

  cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
}
