# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=prodlim
_pkgver=2026.03.11
pkgname=r-${_pkgname,,}
pkgver=2026.03.11
pkgrel=1
pkgdesc='Product-Limit Estimation for Censored Event History Analysis'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL-2.0-or-later')
depends=(
  r-data.table
  r-diagram
  r-lava
  r-rcpp
  r-rlang
  r-ggplot2
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('5c3d7d11a43295031767558ce1eed2a3')
b2sums=('00faf06cff4fec879d4ac0f36ddfebe24ad6cd0116179babf423a1b35d6fd09644e0d0cb2acca4eb57ebc63a505d092ed410230a0da6bae5062170d0b9054ae4')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
