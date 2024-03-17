# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=processx
_pkgver=3.8.4
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Execute and Control System Processes"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r-ps
  r-r6
)
optdepends=(
  r-callr
  r-cli
  r-covr
  r-curl
  r-debugme
  r-rlang
  r-testthat
  r-webfakes
  r-withr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('57e96dd74090594f1b1a63ec1d59091b')
b2sums=('a5657b616af5cfd1a911ff4c5d9f61c7cf75aa4cb0f4580eee3f4686e8dc39e40bd19132f44ec28cb32db0f789443c2c5c342a7e6d2065078f13f38dbb34aa99')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"

  install -d "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "/usr/lib/R/library/$_pkgname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"
}
