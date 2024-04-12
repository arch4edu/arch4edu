# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=truncdist
_pkgver=1.0-2
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=7
pkgdesc="Truncated Random Variables"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-evd
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('673ac340b9edb85504a3f660b5ba18f2')
b2sums=('627c3e236c5d4c5f769cca53066b2d0069534a21171c9bdb5d8340ebf1f303ccfc593241cd1db2319ae423e21671face34b920627366d5bd8dd2fdde38faf5c2')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
