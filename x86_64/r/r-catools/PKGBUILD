# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Sauliusl <luksaulius at gmail>
# Contributor: fordprefect <fordprefect@dukun.de>

_pkgname=caTools
_pkgver=1.18.2
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=11
pkgdesc="Tools: Moving Window Statistics, GIF, Base64, ROC AUC, etc"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-only')
depends=(
  r-bitops
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('c95edd3f71a8fe1ad2cfd0ae274ad9ab')
b2sums=('08f22212ac7ee006d6ea39f7f8fb03ce3d8293f7a36800cb3c65ba577638495dfd2bf0e6a9a6dd7f19b873c42a6a8bb1f2b22c3ae07e4428c288278aebdf62e5')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
