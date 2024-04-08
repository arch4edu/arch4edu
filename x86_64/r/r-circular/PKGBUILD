# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=circular
_pkgver=0.5-0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
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
md5sums=('30ab87f09139540dec4dfdd933c5aff9')
b2sums=('18c59f2ee190111e8aed21f1b95158c94eb2644bbe1cf343aa2a14c90f890090795434f57c875103c105698cb2eb0904f3be2719661598f0b4e184d7b99ebc67')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
