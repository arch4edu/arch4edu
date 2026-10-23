# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=lava
_pkgver=1.10
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Latent Variable Models"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('Apache-2.0')
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
  r-future
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
  r-quarto
  r-rgl
  r-rgraphviz
  r-rmarkdown
  r-svglite
  r-targeted
  r-testthat
  r-vdiffr
  r-visnetwork
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('4e6838bc519c00a8dc00e615a3b226e7')
b2sums=('217f86bb6829ff5bf11d739579d6a3409d04ffcae21b659b69c6e0dadeda369799d22d621144eb752c35aa11ca37081ce6f5bd672c34a1d503537af76cd6a16c')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
