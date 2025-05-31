# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=prodlim
_pkgver=2025.04.28
pkgname=r-${_pkgname,,}
pkgver=2025.04.28
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
md5sums=('eca7064bb5d9fc2a36a792ab99b4ec69')
b2sums=('bf2125a47a1827cd77dea7a409a87fb2f44fda6ff1419a61d59dd10d5c444cf1e5d7fecd9646476e84a231fe9561f24879b250571acadcd2449edeadac0d1505')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
