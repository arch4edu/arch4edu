# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=kernlab
_pkgver=0.9-32
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=5
pkgdesc="Kernel-Based Machine Learning Lab"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  blas
  lapack
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('024ddb451bb525a61e5d17d43c52f400')
b2sums=('ffe623badfe522182492dc5c8bc90872018a6c5d6744cc89e4ba7856c2e7981658788a4ba537d087cf9ef544192a3b2438c8eb51a0abff74e46266cbb6bb66ab')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
