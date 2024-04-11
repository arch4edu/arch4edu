# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=jmvcore
_pkgver=2.4.7
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="Dependencies for the 'jamovi' Framework"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-base64enc
  r-jsonlite
  r-r6
  r-rlang
  r-stringi
)
optdepends=(
  r-fastmap
  r-ggplot2
  r-knitr
  r-ragg
  r-rcolorbrewer
  r-rprotobuf
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('f27afb95f291240751e3f530c16b6e28')
b2sums=('0de0dc4fe2957233ba8f58b60aa59f6d2addaa45b0399d010fe557abd5d23051c474d6c9a415085f3652ccb1fec171ef669e27e9533d87fe8b2e077ea773a011')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
