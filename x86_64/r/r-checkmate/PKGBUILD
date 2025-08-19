# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=checkmate
_pkgver=2.3.3
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
md5sums=('12a890e8191574cd0975fae055371fa5')
b2sums=('e924bb90f64d941fcd1e82941b57fecb48b9797addcc52c461a97493695845acea931c6a43543ca8c142fa56574af69c7d204d313fc957c703bb5f72edc4b0b2')

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
