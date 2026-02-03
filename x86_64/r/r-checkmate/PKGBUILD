# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=checkmate
_pkgver=2.3.4
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
md5sums=('64da20583ae2453fe1c86df562eb031b')
b2sums=('cd592555a4574d04dbc7083b91ee0d37b05050d0e5a0cac1a5d405e07306f0c1beaaf58813f9f94ab77d22658f3b216d8e3abfba86a21925da9217b4ffa13f21')

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
