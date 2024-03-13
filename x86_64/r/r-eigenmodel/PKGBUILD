# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=eigenmodel
_pkgver=1.11
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=9
pkgdesc="Semiparametric Factor and Regression Models for Symmetric Relational Data"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('530e52dd3cad43259c438c6c1d4397d1')
b2sums=('50c8d343146e7caeb1f328c45904dc480d13cace4930de85cce76a8bf157903a318980a09e498c9639566731c7a0aa3ff4e8a978d39104cceb0cd391542d8579')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
