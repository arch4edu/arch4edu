# Maintainer: AutoUpdateBot <auto_update_bot@arch4edu.org>

_pkgname=DistributionS7
_pkgver=0.1.3
_commit=bd346e42fe555858d68b24f6580fa6abf96192b8
pkgname=r-distributions7
pkgver=$_pkgver
pkgrel=1
pkgdesc="Probability distributions with the S7 class system"
arch=(any)
url="https://github.com/Kucharssim/$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r
  r-assertthat
  r-generics
  r-ggplot2
  r-ggrepel
  r-gnorm
  r-goftest
  r-nortest
  r-patchwork
  r-rlang
  r-s7
  r-sgt
  r-sn
)
source=("$_pkgname-$_pkgver.tar.gz::https://github.com/Kucharssim/$_pkgname/archive/$_commit.tar.gz")
md5sums=('494c6d115ab419204b821f6d8712b6ba')
b2sums=('d2f9e73399129820be9c2078ef2c4cfbe3ff19474413bd48d0e8074bc67a2b7c981cb2ba2d442660894c9f2126f99b8b82268dd45fc4cf7e6af7b70b5c9cc7d9')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname-$_commit"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
