# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=mclogit
_pkgver=0.9.6
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=4
pkgdesc="Multinomial Logit Models, with or without Random Effects or Overdispersion"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  r-memisc
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('fde8195c54f7096ebf8071b67b44ddab')
b2sums=('87d0ea35af0f725c27f7a5393854b30d797c99c8c4e598f5f5d17ed889d7e54df59bc7ee9ccaab2a4e59f02cd75a7de71a7d5819e438b7f23d52010b46f0a434')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
