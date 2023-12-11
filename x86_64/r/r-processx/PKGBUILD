# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=processx
_pkgver=3.8.3
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Execute and Control System Processes"
arch=(x86_64)
url="https://cran.r-project.org/package=${_pkgname}"
license=(MIT)
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
md5sums=('ad4eef6b9a21f570f8686c0157712ddf')
sha256sums=('1ad8c51482b89702fbbb6621b1a179c1ae67b78388b8fd9c841bbc8cf035d831')

build() {
  mkdir -p build
  R CMD INSTALL "$_pkgname" -l build
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"

  install -d "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "/usr/lib/R/library/$_pkgname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"
}
