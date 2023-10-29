# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=lava
_pkgver=1.7.2.1
pkgname=r-${_pkgname,,}
pkgver=1.7.2.1
pkgrel=1
pkgdesc='Latent Variable Models'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-future.apply
  r-numderiv
  r-progressr
  r-squarem
)
optdepends=(
  r-bookdown
  r-data.table
  r-ellipse
  r-fields
  r-geepack
  r-graph
  r-igraph
  r-kernsmooth
  r-knitr
  r-lavasearch2
  r-lme4
  r-matrix
  r-mets
  r-nlme
  r-optimx
  r-polycor
  r-quantreg
  r-r.rsp
  r-rgl
  r-rgraphviz
  r-rmarkdown
  r-targeted
  r-testthat
  r-visnetwork
  r-zoo
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('d42b1f5c7e4e76718e4f014c44608295f82b5de0eb25ce8e9b35c40c7839ef2e')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
