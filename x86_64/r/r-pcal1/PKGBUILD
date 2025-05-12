# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=pcaL1
_pkgver=1.5.9
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="L1-Norm PCA Methods"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-or-later')
depends=(
  blas
  coin-or-clp
  lapack
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('4f486874be86c1d141666d56b4f9f37c')
b2sums=('dfb1be5d3baba5cdee806dc15a430302e1e5abe031420b12cfa2fe604ae6c17c3fd7b9796d77b10bd8b5ac1388cabfeb78a3f9f2a88b3a29b51aa0add39aad69')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
