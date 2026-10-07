# Maintainer: AutoUpdateBot <auto_update_bot@arch4edu.org>

_pkgname=tstoml
_pkgver=0.0.0.9000
_commit=548e2e71195906584b17ac0aa83e4d3edcef8da2
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Edit TOML files"
arch=(x86_64)
url="https://github.com/gaborcsardi/$_pkgname"
license=('MIT')
depends=(
  r
  r-tsitter
)
source=("$_pkgname-$_pkgver.tar.gz::https://github.com/gaborcsardi/$_pkgname/archive/$_commit.tar.gz")
md5sums=('32abf8390b3b359f4012a517da8971f7')
b2sums=('3c5dbaabd230a10eab966c8ca17370c28a0cb989f31459d66729a9c8b14fc5392a63db01ff8e5d47b31a23418807be0e255061aad5e419a59cf3356845b9fd69')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname-$_commit"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"

  install -Dm644 "$_pkgname-$_commit/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
