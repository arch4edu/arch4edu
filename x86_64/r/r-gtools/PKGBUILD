# Maintainer: dhn <neilson+aur@sent.com>
# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>
# Contributor: Nick B <Shirakawasuna at gmail _dot_com>

_pkgname=gtools
_pkgver=3.9.5
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="Various R Programming Tools"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
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
b2sums=('f63d2b04d2c62d25d6f45b4ad96fcddadbfee7457c09b5abb82a9ebab205a74003935273df1358e72549b1ff9a1f6178576f3784826ccaf99aaf3ae993801240')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
