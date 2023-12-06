# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=httpuv
_pkgver=1.6.13
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="HTTP and WebSocket Server Library"
arch=(x86_64)
url="https://cran.r-project.org/package=${_pkgname}"
license=(GPL)
depends=(
  libuv
  r-later
  r-promises
  r-r6
  r-rcpp
  zlib
)
checkdepends=(
  r-curl
  r-testthat
  r-websocket
)
optdepends=(
  r-callr
  r-curl
  r-testthat
  r-websocket
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz"
        "link-zlib.patch")
md5sums=('7229873a363a999055f885867c4a69c5'
         'b2a2549bfef0d3a442b6ed545fc2f1f9')
sha256sums=('cb6ef97bb58a062626ed0e7a6cfbc604f82ebd698daa4641c59166b2ab683b5f'
            '95c708ea54de715494bcb43d40973296fb2ee8fb066fb582bfc69cdaf5d4e667')

prepare() {
  # link to zlib
  patch -Np1 -i link-zlib.patch
}

build() {
  mkdir -p build
  R CMD INSTALL "$_pkgname" -l build \
      --configure-vars=USE_BUNDLED_LIBUV=false
}

check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" LC_TIME=C NOT_CRAN=true Rscript --vanilla testthat.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"

  install -d "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "/usr/lib/R/library/$_pkgname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"
}
