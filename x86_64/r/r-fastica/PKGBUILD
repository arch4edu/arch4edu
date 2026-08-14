# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=fastICA
_pkgver=1.2-8
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
md5sums=('a5bb0ead6ebbdf58bf5b1f8e29e36ba7')
b2sums=('5f5ce27e0ee72059f9cd7a638b3b0618c54fe67d8e1a8ad85d00adc297db88cb971438e40705be1e592d53575b9bc02ff6c825af9718b385fd39403ee9614933')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
