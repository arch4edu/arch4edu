# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Sauliusl <luksaulius at gmail>
# Contributor: fordprefect <fordprefect@dukun.de>

_pkgname=caTools
_pkgver=1.18.3
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
md5sums=('cf1ba4c24b336db45c98084ad282a25f')
b2sums=('ff6a66c48b11d51dee0877bf49f577b3724c029fc336bbf08d836dc6ebf1522f458890d7da1e688b66505020f33d138ff242c400bd9a2e827f9aa668dc1cdb89')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
