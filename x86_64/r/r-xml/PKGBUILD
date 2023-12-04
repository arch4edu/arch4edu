# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Alex Branham <branham@utexas.edu>
# Contributor: fordprefect <fordprefect@dukun.de>
# Contributor: Nick B <Shirakawasuna at gmail _dot_com>

_pkgname=XML
_pkgver=3.99-0.16
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="Tools for Parsing and Generating XML Within R and S-Plus"
arch=(x86_64)
url="https://cran.r-project.org/package=${_pkgname}"
license=(BSD)
depends=(
  libxml2
  r
)
optdepends=(
  r-bitops
  r-rcurl
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz"
        "fix-build.patch")
md5sums=('afa1fd1496595b5aa4f6cb758bad0122'
         'fe644b51ff4b55a2b594a6c7dda5bc25')
sha256sums=('350d37bab99ba3dac03313fa3901cc053ab2d962a94a9c3404fb3ad0a91cc95b'
            '5fd93db9dbd4100d4db55714c62340b025d0a871eaf61bffe145fb743e5d26da')

prepare() {
  # fix build
  patch -Np1 -i fix-build.patch
}

build() {
  mkdir -p build
  R CMD INSTALL "$_pkgname" -l build
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"

  install -d "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "/usr/lib/R/library/$_pkgname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"
}
