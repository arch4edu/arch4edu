# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=hypergeo
_pkgver=1.2-15
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="The Gauss Hypergeometric Function"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  r-contfrac
  r-desolve
  r-elliptic
  r-rcpp
)
makedepends=(
  r-rcpparmadillo
)
optdepends=(
  r-magrittr
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('3f8c0b314263d76b708736e179e7e016')
b2sums=('1a7ecc0345e293f526c312c900828d75f2cc36f319fc8d9bb030484d45b8f1a4c7b70360d982107cc9a8abd1b2397796b6b6b60a43f240ce2ffe7daaad98e906')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
