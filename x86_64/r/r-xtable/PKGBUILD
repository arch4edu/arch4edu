# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Alex Branham <branham@utexas.edu>
# Contributor: fordprefect <fordprefect@dukun.de>
# Contributor: Matt Monaco <net 0x01b matt>
# Contributor: Nick B <Shirakawasuna at gmail _dot_com>

_pkgname=xtable
_pkgver=1.8-8
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Export Tables to LaTeX or HTML"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r
)
optdepends=(
  r-knitr
  r-glue
  r-tinytex
  r-zoo
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('4d07e6f65181f7227fac2bd3e6122a0b')
b2sums=('8ccf069f93e9b09a1ab75639328159ee6bb539c9a4e60e1329b519e891d20542ba92ad8ffa43ca63e80b460ffc72cd1d40b3c8e7c0d3b86d7ac545ce432bb020')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
