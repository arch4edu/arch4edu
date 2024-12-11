# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=fastICA
_pkgver=1.2-7
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="FastICA Algorithms to Perform ICA and Projection Pursuit"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only OR GPL-3.0-only')
depends=(
  blas
  lapack
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('0d1346e4402254a585610eab6cf1fa0d')
b2sums=('ea3e8613b795f1cf65184012cdeb738fcaaf071b59ca8bca79a51ac1b8b537753c1bc8e74d234c555d3be1b7e31254e1b081f5bae9cb0156d8364b2c07f761ab')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
