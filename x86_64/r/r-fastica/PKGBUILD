# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=fastICA
_pkgver=1.2-5
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
md5sums=('1b1d258097003be78917f9d8aa448fd6')
b2sums=('d28d11120c239b738ad09ad8cf5cf0c7619800d960ea2c88b74b4b8af660f103f62624a299106108a98e2be73164232bf4b44f14d8e5d1489b524f79c0c13781')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
