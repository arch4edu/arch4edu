# Maintainer: AutoUpdateBot <auto_update_bot@arch4edu.org>

_pkgname=tsitter
_pkgver=0.2.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Tree-Sitter parsing tools"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r
  r-cli
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('ca1f2435caceb112ef0734284fe38437')
b2sums=('a0b85cf5a26653bc409d00c8c4cc9fe318581964f9fb87a7f1a6d2f6724e33b1568b8ac508757ed2cbe8909e22a07dbef406aa002c40c89d62c848f72e70b47f')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"

  install -Dm644 "$_pkgname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
