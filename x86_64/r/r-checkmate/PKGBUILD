# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=checkmate
_pkgver=2.3.2
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Fast and Versatile Argument Checks"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('BSD-3-Clause')
depends=(
  r-backports
)
optdepends=(
  r-data.table
  r-devtools
  r-fastmatch
  r-ggplot2
  r-knitr
  r-magrittr
  r-microbenchmark
  r-r6
  r-rmarkdown
  r-testthat
  r-tibble
  r-tinytest
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('95849df2e80c38e37528a7dbbbbf31cc')
b2sums=('53d396c7ffa49db9edc37c71907a083b24e502758db86c8fb5de490853e66b5096d7ed78d50d5df98d8b6fe7eec0aa11b018e714881df0cbdd86aee349f75892')

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
