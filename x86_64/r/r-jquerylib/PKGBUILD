# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=jquerylib
_pkgver=0.1.4
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//[:-]/.}
pkgrel=7
pkgdesc="Obtain 'jQuery' as an HTML Dependency Object"
arch=(any)
url="https://cran.r-project.org/package=${_pkgname}"
license=(MIT)
depends=(
  r-htmltools
)
checkdepends=(
  r-testthat
)
optdepends=(
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('3607a34ac45ff420bc325d84eab4b0cb')
sha256sums=('f0bcc11dcde3a6ff180277e45c24642d3da3c8690900e38f44495efbc9064411')

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

  install -d "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "/usr/lib/R/library/$_pkgname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"
}
