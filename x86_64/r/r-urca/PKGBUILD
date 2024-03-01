# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=urca
_pkgver=1.3-3
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=3
pkgdesc="Unit Root and Cointegration Tests for Time Series Data"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r
)
makedepends=(
  gcc-fortran
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('cd705f0c6b3599b496af5faca812a879')
b2sums=('dd353ff98ba851377357a012b33a04baec18b7d30151b6320ab39b4dd03ce48c017142ff8fb4e3f4a5abc541608cb0bd16b58802c476f5d552e36259c069c545')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
