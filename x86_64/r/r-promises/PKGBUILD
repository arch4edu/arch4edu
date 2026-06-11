# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=promises
_pkgver=1.5.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Abstractions for Promise-Based Asynchronous Programming"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r-fastmap
  r-later
  r-lifecycle
  r-magrittr
  r-otel
  r-r6
  r-rlang
)
checkdepends=(
  r-future
  r-testthat
)
optdepends=(
  r-future
  r-knitr
  r-mirai
  r-otelsdk
  r-purrr
  r-rcpp
  r-rmarkdown
  r-spelling
  r-testthat
  r-vembedr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('365a4097be36772605653818da60eae6')
b2sums=('10f2f90785e56e8e2c133651bb47214ff408a8bdafe54c79646d7d143a70e6089263e0952afc4e5af1d978c4e15dd4c62fe077cfda5e0fd48832b00d22bdb670')

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
