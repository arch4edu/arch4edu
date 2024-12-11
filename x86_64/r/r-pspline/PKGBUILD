# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=pspline
_pkgver=1.0-21
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
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
md5sums=('9c14307acfb0417f3be76bb293941ca0'
         'd5a357f0c20cfc67aa3d7321a7f25668')
b2sums=('2f288f959fdf1a1c30bb515b56777867e7be9cd9137cae2cc15cfa2384a0d9f14aba6a19c6d06acffa6149d278f70b501e35b5372920c6ee0d241e0115558277'
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
