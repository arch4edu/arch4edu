# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=lava
_pkgver=1.8.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Latent Variable Models"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-only')
depends=(
  r-cli
  r-future.apply
  r-numderiv
  r-progressr
  r-squarem
)
optdepends=(
  r-data.table
  r-ellipse
  r-fields
  r-geepack
  r-graph
  r-igraph
  r-knitr
  r-lavasearch2
  r-lme4
  r-mets
  r-optimx
  r-polycor
  r-quantreg
  r-rgl
  r-rgraphviz
  r-rmarkdown
  r-targeted
  r-testthat
  r-visnetwork
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('3e67327f96b08caeac828871968a4f8b')
b2sums=('3378f30b830846d7979cee57553746ad3735d318ffafe769fbf362df00ed8984e0164df30e06744292666c01bd15e6695638080ef491f4e1c6ced3a2c60918e8')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
