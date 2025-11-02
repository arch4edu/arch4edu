# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=lava
_pkgver=1.8.2
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
md5sums=('41048d6656644a5cdfa70b7e3d4c1d1a')
b2sums=('09cc57f5c596a3c3d055a1294a99223d3312cebb79254c8833a4e05edb164dada47b3fa470a246656200fcfef5df3fa50f3586f6c729056a55a0dd7b0bae2cb0')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
