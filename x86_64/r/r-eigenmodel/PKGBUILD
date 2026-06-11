# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=eigenmodel
_pkgver=1.12
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Semiparametric Factor and Regression Models for Symmetric Relational Data"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('5859fe11bba9998f8bfd814d2f8d8b93')
b2sums=('9ca48862c7d45f269ec71f4c91847b139ab666d1ae3f6b29e640ae563628f6bbf421cfb5941204f74d28002547887af62a91f2021568f1266022559607c2ca6d')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
