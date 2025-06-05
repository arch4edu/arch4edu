# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=RhpcBLASctl
_pkgver=0.23-42
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=4
pkgdesc="Control the Number of Threads on 'BLAS'"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('AGPL-3.0-only')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('825ec304404cad180a6bfb5aef5204b7')
b2sums=('9e6f8471be6f26dafd764d4de8f6c1e1d0685edd851e7e0acc7972d64c3b89336df0df6bfc18616ef7759531134c1c42984f6e4dc9bc096c58497efbcabeee0f')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
