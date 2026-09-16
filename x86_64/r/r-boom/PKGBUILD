# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=Boom
_pkgver=0.9.17
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Bayesian Object Oriented Modeling"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('LGPL-2.1-only')
depends=(
  r
)
optdepends=(
  r-testthat
  r-zoo
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('e1e2ff14c52014685c9698dab8c85a39')
b2sums=('06b1b3e4cbe357bc44e29a3f20dbc9b91647ed50384abf02c0204f567124254f8de5446f10e4fc9b811ef7ea885cf8d27687234f2db4f49739b5b6ea448e739d')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
