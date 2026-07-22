# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=timeSeries
_pkgver=4052.112
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Financial Time Series Objects (Rmetrics)"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-timedate
)
optdepends=(
  r-ftrading
  r-performanceanalytics
  r-robustbase
  r-runit
  r-xts
  r-zoo
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('7c423b828785c9ae0b11648e7aa3d156')
b2sums=('554879a0fb852b50aa64e93d34292eed8532074a9d0eff4de58a1a80219e860a0f6e83d8decd942d500f32aa0c42a2824fb9a8e07eafe01ea24b61b56d80fc72')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
