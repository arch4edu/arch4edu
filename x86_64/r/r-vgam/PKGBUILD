# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=VGAM
_pkgver=1.1-9
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="Vector Generalized Linear and Additive Models"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=(GPL3)
depends=(
  r
)
makedepends=(
  gcc-fortran
)
optdepends=(
  r-vgamextra
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('f51f80d9943e8773bfb12a5139151b2e')
b2sums=('759aa1a780bd64ac7b8d8289c8031ddc20cde5f82a20cdc6d049712a38016fd7107d6931431c88bae660468e5e480d485ce95126fa992c4b6fd376034ed86f2b')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
