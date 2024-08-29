# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=circular
_pkgver=0.5-1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Circular Statistics"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  r-mvtnorm
)
makedepends=(
  gcc-fortran
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('f75fc34ace079f28f6ed1e5fec6f978f')
b2sums=('c4999c4b9e090a6326fcb615e4fb0dc089aeaa2b29ca3e46cbfb1eebc01ab0de5e7cfcdb80011621e11f579e460323af05c0bccd026335f21499f52ed69fb491')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
