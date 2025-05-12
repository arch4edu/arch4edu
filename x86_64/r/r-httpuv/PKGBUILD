# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=httpuv
_pkgver=1.6.16
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
md5sums=('d765d1c8e8131cc5f737edf93c4d0a5b'
         'b2a2549bfef0d3a442b6ed545fc2f1f9')
b2sums=('49ad3db2b2776b6b80c9a965c39054c1a45fe6b9d8dd42d86dc54af5c3e7d7ab7959c24bac8185c5fa71e00c949189d346646bbd13586c7e425a3339e009871a'
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
