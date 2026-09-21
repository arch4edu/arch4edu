# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=weibullness
_pkgver=2.26.9
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Goodness-of-Fit Test for Weibull Distribution (Weibullness)"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only OR GPL-3.0-only')
depends=(
  r
)
optdepends=(
  r-bsgof
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('10ab3669a9173ca3618a57d02661ec34')
b2sums=('87de21332d15ff1ee5d06b27074b81bd873791da334066e9f703b197427325b93aa62f023823b4c1770ad8dc927110e45190c9e191880dc160669fa40370b21e')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
