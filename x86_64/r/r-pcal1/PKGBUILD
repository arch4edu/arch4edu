# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=pcaL1
_pkgver=1.5.7
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=3
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
md5sums=('3e92f99030a222ee3a6c93ca93d51c69')
b2sums=('abe0db99571a5fe056c44be570cbf9b7a5f5804e1efe302a46f4ba77ec06e012e2a01ebf643ef70d93f5d75e5c02e32bd714ea51f2370bad0ed04ff74ac405ec')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
