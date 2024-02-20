# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=estimability
_pkgver=1.5
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Tools for Assessing Estimability of Linear Predictions"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-or-later')
depends=(
  r
)
optdepends=(
  r-knitr
  r-rmarkdown
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('36a7cd52f48a9421d8152cc2e814f603')
b2sums=('681d81d3d931b575401dae6f3fb427d44c266c7dcabaa0c5de7db319e499f27b12a5fdbb415c14fd7abad17779b07c18dad8c897ffa4a4509978dbb09dc5746a')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
