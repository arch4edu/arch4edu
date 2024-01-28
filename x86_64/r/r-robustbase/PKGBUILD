# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Alex Branham <alex.branham@gmail.com>

_pkgname=robustbase
_pkgver=0.99-2
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
md5sums=('1b79921bca8334ef03f67f0ca0afd63f')
b2sums=('977547562f85831fb712f5aacc79a6d2c8fb223dedd50b196e1e4e4196dccaa1e8eac1de27b9b9bf96c10c69f26720fb9260909f808b46ded1d039675aaf8138')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
