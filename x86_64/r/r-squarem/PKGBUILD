# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=SQUAREM
_pkgver=2021.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=12
pkgdesc="Squared Extrapolation Methods for Accelerating EM-Like Monotone Algorithms"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=(GPL)
depends=(
  r
)
optdepends=(
  r-setrng
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('529ce81903111315c68131f0452a939f')
b2sums=('2be8b6f40e8c1c3b0709966a9a4d88e742a7ebefbb571fb2a9eadf1ee067acc992ecf6fa08fa0322aa74182e90d5a9a58403ce94639ae80ad24a2163c05d05d9')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
