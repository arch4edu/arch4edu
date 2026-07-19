# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: peippo <christoph+aur@christophfink.com>

_pkgname=asciicast
_pkgver=2.3.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=6
pkgdesc="Create 'Ascii' Screen Casts from R Scripts"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r-cli
  r-curl
  r-jsonlite
  r-magick
  r-processx
  r-tibble
  r-v8
  r-withr
)
_checkdepends=(
  r-cpp11
  r-decor
  r-htmlwidgets
  r-mockery
  r-rmarkdown
  r-testthat
)
optdepends=(
  r-callr
  r-covr
  r-cpp11
  r-decor
  r-htmlwidgets
  r-knitr
  r-mockery
  r-rmarkdown
  r-rstudioapi
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz"
        "skip-tests.patch")
md5sums=('578583bc17279b6a9b29fa8901f5849c'
         'a9dcfc31b1ed44cffc9ded23922b4b4d')
b2sums=('15827cc88d3e715fb0600d257df06834b4d813c56cc43517252784b007e5ee2734f321fe98386ef8287237703fb6c3e27ff4234804bbe7b67651d02bbc779859'
        'eb06846ca9ffd5fd84ab8b7d83b57376dea7fff7920b90c2d14e6814478019d4be4a57382591fb3af8204923e91ce607f96765f3c72900acbe87efcd6fc0e356')

prepare() {
  # skip tests that need phantomjs
  patch -Np1 -i skip-tests.patch
}

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

_check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" NOT_CRAN=true Rscript --vanilla testthat.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"

  install -d "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "/usr/lib/R/library/$_pkgname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"
}
