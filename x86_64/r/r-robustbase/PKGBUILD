# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Alex Branham <alex.branham@gmail.com>

_pkgname=robustbase
_pkgver=0.99-0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="Basic Robust Statistics"
arch=(x86_64)
url="https://cran.r-project.org/package=${_pkgname}"
license=(GPL)
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
md5sums=('03172533b8059f9da2ae781aa236c032')
sha256sums=('437d422eec29c4345ea65efa6b2c7c21944059a79643d74f4187e06db6e35077')

build() {
  mkdir -p build
  R CMD INSTALL "$_pkgname" -l build
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
