# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=juicyjuice
_pkgver=0.1.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Inline CSS Properties into HTML Tags Using 'juice'"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r-v8
)
optdepends=(
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('bf3db84d36b3734e9c323eb0e9b0b4a3')
b2sums=('bbd13cb4d72b37f327919725fa76dfbfe5232d355694456fc5e127fb690c32caf6628831a7afdc63cd7920d08ecb54683bbeed50e65b2c551a5903f0fd0f3a63')

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
