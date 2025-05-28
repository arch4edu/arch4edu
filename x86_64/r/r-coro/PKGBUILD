# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=coro
_pkgver=1.1.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="'Coroutines' for R"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r-rlang
)
optdepends=(
  r-knitr
  r-later
  r-magrittr
  r-promises
  r-reticulate
  r-rmarkdown
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('7098e0517f4d67246c3d6db5f3ddffb4')
b2sums=('9a31369e919d5a378800c7f30bff8e0cbc9bfc93d42e3bbb3b8efa1ec04b8d4b1fe5ee2a9a2def35134777e32c8b24d7599b5540a0a2627c5f9173407b67a13f')

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
