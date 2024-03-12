# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=wesanderson
_pkgver=0.3.7
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="A Wes Anderson Palette Generator"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r
)
optdepends=(
  r-ggplot2
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('8becbb8ab06d2c694c06d0a1b10da95b')
b2sums=('7fb2db1777ccf60ded0fa4e11079705c5c98a566a51ec88c911e5c64573c3a679102e8aa38e967decefe554b0504ea37628e89a391095ee8707e6d9296d49b54')

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
