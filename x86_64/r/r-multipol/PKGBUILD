# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=multipol
_pkgver=1.0-9
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=4
pkgdesc="Multivariate Polynomials"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-abind
)
optdepends=(
  r-polynom
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('d3a4bfaf81932f44018a064c7ae3b5c8')
b2sums=('c70fa60813fe0b0aa1d358532a961cd880f6e661785504201f9d983b8f980e7c25d9b089f84c2671a893e51589d32925008ba3142dfa3336dcfe232c57339581')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
