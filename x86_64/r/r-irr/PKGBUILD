# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=irr
_pkgver=0.84.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=7
pkgdesc="Various Coefficients of Interrater Reliability and Agreement"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-lpsolve
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('802ae19d1fc45cede1afafb5012cfdf0')
b2sums=('41f6e4046a498394cb53a1c4599a7ac6ec66b9301272f7bb523740887bd8c8ed3b23a74c48e5eb177042c36a9f968fb7e47b55426ea1318a71183c01e4c537fa')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
