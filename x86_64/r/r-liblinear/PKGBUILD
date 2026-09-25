# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=LiblineaR
_pkgver=2.10-26
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Linear Predictive Models Based on the LIBLINEAR C/C++ Library"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  r
)
optdepends=(
  r-knitr
  r-rmarkdown
  r-sparsem
  r-spelling
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('1132173157eec3991b118b55e15e2d81')
b2sums=('31f35197bff8bc2c9b32640fe7f87e8023d28d07612121632ad4e31ed24602082449ded5107dcddd3e77b47c99b84429c91615699f1c992224e73e9458f9f48b')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
