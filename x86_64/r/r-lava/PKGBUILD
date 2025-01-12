# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=lava
_pkgver=1.8.1
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
md5sums=('d09dd78ac2364d14c2b8931bd6bdd574')
b2sums=('ca05d1940685327de7d8055875705ab3d1d7991253a6d3ed869aeee4473bb89d86e762eca5ff62c44dfc283d6e356210b7c3b9f342ae9e15c3f08338cf32e263')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
