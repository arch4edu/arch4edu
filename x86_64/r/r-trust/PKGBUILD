# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=trust
_pkgver=0.1-9
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Trust Region Optimization"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('86d07fa891b3c291b358cfc48f5c84ce')
b2sums=('b0cd963f256545510e3a7b01e53c98d9d001aedf9fde79ca1d10c54201b9f38df939ae330bd7515b09d501c35f8ab58bed12b3165c9304f44f833f8510dba996')

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
