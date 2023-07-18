# Maintainer: dhn <neilson+aur@sent.com>
# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>
# Contributor: Nick B <Shirakawasuna at gmail _dot_com>

_pkgname=gtools
_pkgver=3.9.4
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=3
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
md5sums=('e76b59c1eff674bc0bd2e4aa990a9395')
sha256sums=('59cf8b194fe98b1cc05dbb4d686810a1068f59d8b402b731548a898ece85f111')

build() {
  mkdir -p build
  R CMD INSTALL "$_pkgname" -l build
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
