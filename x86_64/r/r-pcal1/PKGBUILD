# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=pcaL1
_pkgver=1.5.7
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="L1-Norm PCA Methods"
arch=(x86_64)
url="https://cran.r-project.org/package=${_pkgname}"
license=(GPL3)
depends=(
  blas
  coin-or-clp
  lapack
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('3e92f99030a222ee3a6c93ca93d51c69')
sha256sums=('23043bf20d3e9c1499578686486c94c5f0cbbc879e4e3b9ea257f34224c1934c')

build() {
  mkdir -p build
  R CMD INSTALL "$_pkgname" -l build
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
