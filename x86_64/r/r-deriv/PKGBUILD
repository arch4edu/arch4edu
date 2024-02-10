# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=Deriv
_pkgver=4.1.3
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=9
pkgdesc="Symbolic Differentiation"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-or-later')
depends=(
  r
)
optdepends=(
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('e4405e9b07cda190696378cf7fb77e71')
b2sums=('bf04f06718243431f2436cca424de285ead05051f2f8ca6a586b4f5ec1e946f630172cdd4bcfd88da6eedb455e52a5649270fd2a5818dbc87e7d056fb4c40aa5')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
