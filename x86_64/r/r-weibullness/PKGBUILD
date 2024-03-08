# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=weibullness
_pkgver=1.24.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
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
md5sums=('3725675d4d305d1ffe3f7ca8d2392132')
b2sums=('e720ac9abe50b74199c74ed717a1b0d5e7f2778eeef5e3b9b1a6b9b94e0781364e10687616d6aeea0d553e385c7384d1cba1d51a273ac40779cacd901e629bd4')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
