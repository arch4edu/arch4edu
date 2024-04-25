# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=mockery
_pkgver=0.4.4
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="Mocking Library for R"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r-testthat
)
optdepends=(
  r-knitr
  r-r6
  r-rmarkdown
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('98297a49097c3c952c9321de4710df7f')
b2sums=('9a19ce9ffe07413132945c2a9c9cb1760f9910712be7598ab5ba3d9267cf85cecd40e0b5578d2f5b274157a201c5b5d90f1795c8cdfdb4a989d3e454a5b0fa6c')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
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
