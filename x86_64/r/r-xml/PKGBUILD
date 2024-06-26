# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Alex Branham <branham@utexas.edu>
# Contributor: fordprefect <fordprefect@dukun.de>
# Contributor: Nick B <Shirakawasuna at gmail _dot_com>

_pkgname=XML
_pkgver=3.99-0.17
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
md5sums=('88b6598cf17176e215ade9a3055a275d')
b2sums=('2209b2c07cde71dc59489b52920d9db983b2243d1797b850469a2b470b67651b74189f268d4cbaf16e4446db7a814b8f3c8c81a897f7eb6b5460861df31da0f2')

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
