# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=fracdiff
_pkgver=1.5-3
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="Fractionally Differenced ARIMA aka ARFIMA(P,d,q) Models"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  blas
  r
)
optdepends=(
  r-forecast
  r-longmemo
  r-urca
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('f709c0a691bc7287bb5ab1f014885a4f')
b2sums=('be61604f7afe4d706402a0906ab4dcdd2d702aaa8250908ebde16657afb2703bf3f4481116701c97fdf0260dafd87e6d2c20a7d2eff11170cbcc47b688615200')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
