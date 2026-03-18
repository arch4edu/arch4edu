# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=httpuv
_pkgver=1.6.17
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="HTTP and WebSocket Server Library"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later AND MIT')
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
  r-jsonlite
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz"
        "link-zlib.patch")
md5sums=('50763765704e547c15aac4be97cec437'
         'b2a2549bfef0d3a442b6ed545fc2f1f9')
b2sums=('b0f4be59cbe060ea881de2723ab63de6c2bfbcdd5d89eaccc64825a2488ed77cc2ec38bfde22e1b45198da7c320c586fb45444ad47eb4a1e0a246b3e469b2ad7'
        '8aeff9d8175384692fcf729078e44c98a52d5e70cfc2edf8679b092abe94d6372178b1d6ca28a427b30080e1359e2ebec30db9e089d0e54f9c230ec4e094b99a')

prepare() {
  # link to zlib
  patch -Np1 -i link-zlib.patch
}

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname" \
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
