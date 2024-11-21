# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=ggrain
_pkgver=0.0.4
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=3
pkgdesc="A Rainclouds Geom for 'ggplot2'"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r-cli
  r-gghalves
  r-ggplot2
  r-ggpp
  r-rlang
  r-vctrs
)
optdepends=(
  r-knitr
  r-rmarkdown
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('8e24f1f21eac678fe6b1951e61022701')
b2sums=('ad05d6c4e54e66b56dbffa97d03109ca19fcea26fb2d2fd8c99be408fafd81ab694f756e8fc295904eda20caa8eb94f89c8df03f2c93adc6e8d623e77ed67c35')

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
