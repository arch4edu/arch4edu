# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=svglite
_pkgver=2.1.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=3
pkgdesc="An 'SVG' Graphics Device"
arch=(x86_64)
url="https://cran.r-project.org/package=${_pkgname}"
license=(GPL)
depends=(
  libpng
  r-systemfonts
)
makedepends=(
  r-cpp11
)
checkdepends=(
  r-fontquiver
  r-testthat
  r-xml2
  ttf-liberation
)
optdepends=(
  r-covr
  r-fontquiver
  r-htmltools
  r-knitr
  r-rmarkdown
  r-testthat
  r-xml2
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('95ce45d5f57c8e82b7b2322fbe4868fb')
sha256sums=('48700169eec1b05dbee9e2bae000aa84c544617b018cb3ac431a128cfd8dac56')

build() {
  mkdir -p build
  R CMD INSTALL "$_pkgname" -l build
}

check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" NOT_CRAN=true Rscript --vanilla testthat.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
