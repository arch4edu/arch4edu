# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=randomizr
_pkgver=1.0.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
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
md5sums=('48d39b829955b9c76bd23e0ad926625c')
b2sums=('7395a14bf4bc582f93b819d5c0cb09ec11bccebf4597082e4de97e40c9fc867df6136d72a44e13fe10c96b74c5b91df0552ad1e382fd136af9610c9bd7d7e6d7')

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
