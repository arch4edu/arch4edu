# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=QuickJSR
_pkgver=1.9.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Interface for the 'QuickJS-NG' Lightweight 'JavaScript' Engine"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r
)
checkdepends=(
  r-tinytest
)
optdepends=(
  r-knitr
  r-rmarkdown
  r-tinytest
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('7ee1bebd9ac30505a053f30b6f1e05e4')
b2sums=('42ce932656fd49c44a5c09de0f1048d8fae96ade1a9a680b4b6c4a5f69d40e23b8391066d623e2dec6d1985304cc65b69529a9b2d62c7a194831a3ed2d5091d5')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" Rscript --vanilla tinytest.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"

  install -d "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "/usr/lib/R/library/$_pkgname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"
}
