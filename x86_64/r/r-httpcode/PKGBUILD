# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=httpcode
_pkgver=0.3.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=9
pkgdesc="'HTTP' Status Code Helper"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=(MIT)
depends=(
  r
)
optdepends=(
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('50695b63da6ea32fdffca37cda307fc6')
b2sums=('59bad16c2b394c73305ebdb1b0c781dc7f46c58e3b00d23c77d36baae71f0ee8dd4e9138a8aded73a2a1b217b1dd87f04a7f2c1d992b2f0dfa9c837c43fe2f3f')

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
