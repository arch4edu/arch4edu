# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: peippo <christoph+aur@christophfink.com>

_pkgname=webfakes
_pkgver=1.5.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Fake Web Apps for HTTP Testing"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r
)
optdepends=(
  r-brotli
  r-callr
  r-covr
  r-curl
  r-digest
  r-glue
  r-httpuv
  r-httr
  r-jsonlite
  r-processx
  r-testthat
  r-withr
  r-xml2
  r-zip
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('00dac0b04e174e676867662d079519a4')
b2sums=('2ee67a2810323e5bad08c6bf454ff2a334499ccc975eccded70ae78894addacb25b371beda99a992b6bf6e57a07966feda8c0b16bd6736f1b1d08219b26baf26')

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
