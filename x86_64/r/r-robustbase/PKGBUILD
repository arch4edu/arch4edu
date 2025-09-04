# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Alex Branham <alex.branham@gmail.com>

_pkgname=robustbase
_pkgver=0.99-6
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Basic Robust Statistics"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  blas
  lapack
  r-deoptimr
)
makedepends=(
  gcc-fortran
)
optdepends=(
  r-catdata
  r-doparallel
  r-fit.models
  r-foreach
  r-ggally
  r-ggplot2
  r-mpv
  r-rcolorbrewer
  r-reshape2
  r-robust
  r-sfsmisc
  r-skewt
  r-xtable
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('d261c64ca13181bf5ed1024dfb2e77fc')
b2sums=('68b7d8559a4859e9fdfadf1684b5b3fdacb5bc962c071a6979956ac3d94c5e0cc429e96317858c913a3edc0facfc9e6310ec97d3afd6ce6dd33e539e40ada47b')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
