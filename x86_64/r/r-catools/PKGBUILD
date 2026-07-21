# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Sauliusl <luksaulius at gmail>
# Contributor: fordprefect <fordprefect@dukun.de>

_pkgname=caTools
_pkgver=1.18.4
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Tools: Moving Window Statistics, GIF, Base64, ROC AUC, etc"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-only')
depends=(
  r-bitops
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('e8e44f4da77b1d95935b0683f2944628')
b2sums=('00df3dfcf1232f6743d6b33d1fec2cb2e202b821ba7f1d810099881667401509d1f76e316d1a57ac6becf0252778c5bf87ed825985fc859a9d4c6c0f1128776a')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
