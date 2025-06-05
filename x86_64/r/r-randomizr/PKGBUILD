# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=randomizr
_pkgver=1.0.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="Easy-to-Use Tools for Common Forms of Random Assignment and Sampling"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r
)
optdepends=(
  r-dplyr
  r-knitr
  r-rmarkdown
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('7860c9a6c26008f6d4ebbcfc01ce911b')
b2sums=('6c019790940fb069a2b0ea6090d248c5cd6d38c0e28b52fbf516400b42164ba57dacfec3b85cb98dc1179ac1f47e7eb3f88ba124fd9b60f8d1916da7c961ca91')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"

  install -d "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "/usr/lib/R/library/$_pkgname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"
}
