# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=vegan
_pkgver=2.6-8
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Community Ecology Package"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  lapack
  r-permute
)
makedepends=(
  gcc-fortran
)
optdepends=(
  r-knitr
  r-markdown
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('37242afddc710d26bd7934072c1e100a')
b2sums=('4e8a4253bf32b1954351a3d4954d3a9f838a11e31e46a73d3c5742de1679aa4574a89cff502c282618248262a1e1954dd3c347436e1a5f0d68b25482b54dde30')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
