# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=circular
_pkgver=0.5-2
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Circular Statistics"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  r-mvtnorm
)
makedepends=(
  gcc-fortran
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('4f33e7d8a9ac8184dccb87533536bef8')
b2sums=('72091ca97b0d1395b3084c0052cc674743c2f866070570eb7f60019c9f94d0c020b1d8e72c08c52626254f0d075951089de5420e0995d48cd19f16292e455e26')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
