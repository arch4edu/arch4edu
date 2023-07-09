# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Alex Branham <branham@utexas.edu>
# Contributor: fordprefect <fordprefect@dukun.de>
# Contributor: Matt Monaco <net 0x01b matt>
# Contributor: Nick B <Shirakawasuna at gmail _dot_com>

_pkgname=xtable
_pkgver=1.8-4
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=10
pkgdesc="Export Tables to LaTeX or HTML"
arch=(any)
url="https://cran.r-project.org/package=${_pkgname}"
license=(GPL)
depends=(
  r
)
optdepends=(
  r-knitr
  r-plm
  r-zoo
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('0a7da6c3b34b2974110a7d00fe9afa79')
sha256sums=('5abec0e8c27865ef0880f1d19c9f9ca7cc0fd24eadaa72bcd270c3fb4075fd1c')

build() {
  mkdir -p build
  R CMD INSTALL "$_pkgname" -l build
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
