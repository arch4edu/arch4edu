# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=pspline
_pkgver=1.0-19
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=6
pkgdesc="Penalized Smoothing Splines"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('LicenseRef-Unlimited')
depends=(
  r
)
makedepends=(
  gcc-fortran
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz"
        "Unlimited")
md5sums=('a2a324253f7a353bb252adbb14fca38b'
         'd5a357f0c20cfc67aa3d7321a7f25668')
b2sums=('2f3aa1bd6aed04a226545278481f5ee3f28bc71dac73e47e3c445405d79b141c47ebf7c1586f9b6d293960d1a89374d5988e8f4583163f4c19f5b19ca3bb5a1c'
        '76d707bdc00cd0ba4a6f5f889db74d5857938783d7a94fd8d605a5eaf6108501bc17198366109faa7ebc52cc934fb0ef6af4a9aa217b625a8dd22ed84dab9eec')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"

  install -Dm644 -t "$pkgdir/usr/share/licenses/$pkgname" Unlimited
}
