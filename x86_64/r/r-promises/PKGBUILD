# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_cranname=promises
_cranver=1.2.0.1
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="Abstractions for Promise-Based Asynchronous Programming"
arch=(i686 x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(MIT)
depends=(r r-r6 r-rcpp r-later r-rlang r-magrittr)
optdepends=(r-testthat r-future r-fastmap r-purrr r-knitr r-rmarkdown r-vembedr r-spelling)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
sha256sums=('8d3a8217909e91f4c2a2eebba5ac8fc902a9ac1a9e9d8a30815c9dc0f162c4b7')

build() {
  R CMD INSTALL ${_cranname}_${_cranver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"

  cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
}
