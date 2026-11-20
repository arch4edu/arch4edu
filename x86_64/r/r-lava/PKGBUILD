# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=lava
_pkgver=1.11
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
  r-mmrm
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
md5sums=('756ce1cbda5c8285881c77a85ff19587')
b2sums=('ea875139bd4d51625bfabf9411277be99305173db49e2f4fb6c3bae3b6a73dc6d3928f4ebe8c59660af8c4440c61ea4031d6bb235b338371a65f7e008689797a')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
