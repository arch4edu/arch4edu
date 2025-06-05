# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=bigassertr
_pkgver=0.1.6
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=4
pkgdesc="Assertion and Message Functions"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-only')
depends=(
  r
)
optdepends=(
  r-covr
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('117e5596df34dc306881809960c2233d')
b2sums=('201f0e4c77894513116e4aaf4dfb5f26b7e0ab4cf1ea225c5a3dd1ae5f30697ce59c9579f810a3f7c3628fff0ec7683ac803619ec3aa8b1b0dd8bdd2e3a70270')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
