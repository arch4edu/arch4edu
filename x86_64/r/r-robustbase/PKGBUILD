# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Alex Branham <alex.branham@gmail.com>

_pkgname=robustbase
_pkgver=0.99-4
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
md5sums=('15217afc9300155086fada9cb02352ab')
b2sums=('b674981181c2a05c58b0c0676c29cae878b46721bbb95a4216fd0546a2ef6db02a287d49448fb1cede6a6db9e5af69939fbbf1da8265ac36edc9d2bbfc8c2639')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
