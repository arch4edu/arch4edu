# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=hexbin
_pkgver=1.28.6
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Hexagonal Binning Routines"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  r
)
makedepends=(
  gcc-fortran
)
optdepends=(
  r-affy
  r-biobase
  r-knitr
  r-limma
  r-marray
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('8222b0f44503b0eab15814641127d9d3')
b2sums=('05fb5975e7400e117bf8cc62d862fb3c22be6fe9265376e205d5ec76ba616ff341299dfdc89518b4fd160a188367159d3cba9f77b700edf2d301ad0da01ebf99')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
