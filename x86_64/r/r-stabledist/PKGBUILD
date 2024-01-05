# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=stabledist
_pkgver=0.7-1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=9
pkgdesc="Stable Distribution Functions"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=(GPL)
depends=(
  r
)
optdepends=(
  r-fbasics
  r-fmstable
  r-rmpfr
  r-runit
  r-sfsmisc
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('0f6159d8f129e4c367a1adc5860079b0')
b2sums=('90166fde731946283e688c632cc013e288bb2a0ab9b58e86cbf0445a0e77a174411fb9683f1c546839cc87e965a16f6880b7ea8642f825d5da084ef475820c83')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
