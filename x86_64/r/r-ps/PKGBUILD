# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=ps
_pkgver=1.7.7
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="List, Query, Manipulate System Processes"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r
)
optdepends=(
  r-callr
  r-covr
  r-curl
  r-pillar
  r-pingr
  r-processx
  r-r6
  r-rlang
  r-testthat
  r-webfakes
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('8c0dd99a89635cb7a8f837f7f0ab6e93')
b2sums=('49e61deccac77a8fd3018eed95530239176f41bfffeb0d9c9ca482dd7b53af1c18d9136cfe9127474c74da1204943fcf0b564d7469dc5b75bbe5d88c1a9fc383')

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
