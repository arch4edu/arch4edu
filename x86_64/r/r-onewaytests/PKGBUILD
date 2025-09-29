# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: sukanka <su975853527@gmail.com>

_pkgname=onewaytests
_pkgver=3.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="One-Way Tests in Independent Groups Designs"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-car
  r-ggplot2
  r-moments
  r-nortest
  r-wesanderson
)
optdepends=(
  r-aid
  r-testthat
  r-tibble
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('0b1d140413abd6aeda7d96843dc90bf4')
b2sums=('5583681efa7f48128f94b25347518af86b82d44faf058bf15d48c61ed79824a9aec246b0ae7ed74e8203c8b23d5130d55005bf424a64dc81d4716b9c2550c6aa')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
