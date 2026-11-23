# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=doFuture
_pkgver=1.4.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Use Foreach to Parallelize via the Future Framework"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('Apache')
depends=(
  r-foreach
  r-future
  r-future.apply
  r-globals
  r-iterators
)
checkdepends=(
)
optdepends=(
  r-dorng
  r-markdown
  r-r.rsp
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('bb250435b5d35c57c0989c52bacf91a5')
b2sums=('0cfff2d9deb6202c55bd6da737f005ef8a3b4ad08565975ae2efdea89925f31b872ef1dd60cad8538359cc33bc8e3b8b97ac478efa61cefe8e6e1774efb79d07')

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
}
