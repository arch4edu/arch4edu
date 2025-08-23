# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Alex Branham <branham@utexas.edu>
# Contributor: fordprefect <fordprefect@dukun.de>
# Contributor: Nick B <Shirakawasuna at gmail _dot_com>

_pkgname=XML
_pkgver=3.99-0.19
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Tools for Parsing and Generating XML Within R and S-Plus"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('BSD-3-Clause')
depends=(
  libxml2
  r
)
optdepends=(
  r-bitops
  r-rcurl
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('a0fd8a9595bd82c7f41a9f3cdf3d3323')
b2sums=('53d0925f4ac7dc0812a8f9f7427feda0ea08210f7a4badab63017e20fbea7eaf9b8cc73b474cc5bd218b7a34f30e719722f38b9e6eed4c3483704b25f4c04ba5')

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
