# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=moments
_pkgver=0.14.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=7
pkgdesc="Moments, Cumulants, Skewness, Kurtosis and Related Tests"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=(GPL)
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('622afd35702c45ad010c106af2457458')
b2sums=('60e12f8a33c051cb91282438d8afb1459882b332ccdde217cdd10cafab32d97084b49a0e670b1716035188d37be7199740ac5baf06ab803309e9586bc7c683b0')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
