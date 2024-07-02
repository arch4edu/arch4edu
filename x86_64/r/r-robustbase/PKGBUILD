# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Alex Branham <alex.branham@gmail.com>

_pkgname=robustbase
_pkgver=0.99-3
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
md5sums=('8fe3a3376c5d0f70efa755aacf46c94e')
b2sums=('47b16e3457390377462a1fba1851be96e632bf046491c736083183479070ef2cbf817a23c23fb98cfeccf29d47c5d469768b7360642ed3986654317086d1ab6b')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
