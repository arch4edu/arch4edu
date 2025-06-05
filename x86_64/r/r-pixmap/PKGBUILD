# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=pixmap
_pkgver=0.4-13
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Bitmap Images / Pixel Maps"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('908e41d62d4943388c6baf07aae1a71f')
b2sums=('5e656748284b1f1b5e457c88cce7693005c490129f3c0870a41ff04d080b11ed0a9011c9506e974903e94a2ca1b8bfdea00bcd43c3690f8d9add38a0fcae0aa9')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
