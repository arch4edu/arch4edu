# Maintainer: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_cranname=rstudioapi
_cranver=0.13
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="Safely Access the RStudio API"
arch=(any)
url="https://cran.r-project.org/package=${_cranname}"
license=(MIT)
depends=(r)
optdepends=(r-testthat r-knitr r-rmarkdown r-clipr)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
sha256sums=('aac35bbdcb4a8e8caba943bc8a2b98120e8940b80cd1020224bb1a26ff776d8b')

build() {
  R CMD INSTALL ${_cranname}_${_cranver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"

  cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
}
