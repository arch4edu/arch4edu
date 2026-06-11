# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=fracdiff
_pkgver=1.5-4
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
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
md5sums=('963d73ba845fabf38a737b6929abecfd')
b2sums=('696f60187cdbb8837f94226b5591db576ffb12015c34f484922d8cc7253fe8032a120002db5af4a2f4b0f45c42c80345bdfe13b62b56d19264e98800cad65a33')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
