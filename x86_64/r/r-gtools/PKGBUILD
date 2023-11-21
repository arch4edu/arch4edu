# Maintainer: dhn <neilson+aur@sent.com>
# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>
# Contributor: Nick B <Shirakawasuna at gmail _dot_com>

_pkgname=gtools
_pkgver=3.9.5
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Various R Programming Tools"
arch=(x86_64)
url="https://cran.r-project.org/package=${_pkgname}"
license=(GPL2)
depends=(
  r
)
optdepends=(
  r-car
  r-gplots
  r-knitr
  r-rstudioapi
  r-sgp
  r-taxize
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('6d7837a6d8b8019e16a7c9eb567899db')
sha256sums=('dee9b6c1152db1a5dc427d074b32bbbb738708683f17a95e0e95e4d79fdf174b')

build() {
  mkdir -p build
  R CMD INSTALL "$_pkgname" -l build
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
