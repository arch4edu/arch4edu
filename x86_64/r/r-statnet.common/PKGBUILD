# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=statnet.common
_pkgver=4.9.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=4
pkgdesc="Common R Scripts and Utilities Used by the Statnet Project Software"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-only')
depends=(
  r-coda
)
optdepends=(
  r-covr
  r-rlang
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('85503e6c3fdaae2040a8c872fcbd8ad6')
b2sums=('6ddfd61a6ec633dff4ddb554eb10e46237a0ae893d078746c56ed6e99353d96b037f76edbb2bacc0229c59663dc544897c9f214b55051d439b780dcbcbcdaf0e')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
