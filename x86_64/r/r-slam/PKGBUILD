# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>

_pkgname=slam
_pkgver=0.1-55
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Sparse Lightweight Arrays and Matrices"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  blas
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('e2a13be23d1c48b0cc1a241c901f3410')
b2sums=('96e715b7b52678204c1c08a61b2d8905cf90acce1c63bbd80063c31b6eb9c58ece5954e406d8356f3e7dc38239ca4fb1e18ddc72e1d2623a4c27ebc92bd8b3bd')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
