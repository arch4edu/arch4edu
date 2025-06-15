# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=gamm4
_pkgver=0.2-7
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Generalized Additive Mixed Models using 'mgcv' and 'lme4'"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-lme4
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('20482b67d00335cf5c975eb9097716a1')
b2sums=('9e71b450003464c853ab6d8e3128f424456076c4bd5399e99e9f4c46964e756e201dee52b7545aca3a847966e17178ec7d2024270d8bd629491b421345be8ad9')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
