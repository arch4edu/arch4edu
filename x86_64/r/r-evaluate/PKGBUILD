# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Kibouo <csonka.mihaly@hotmail.com>
# Contributor: Ward Segers <w@rdsegers.be>
# Contributor: Alex Branham <alex.branham@gmail.com>

_pkgname=evaluate
_pkgver=1.0.5
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Parsing and Evaluation Tools that Provide More Details than the Default"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r
)
optdepends=(
  r-covr
  r-ggplot2
  r-rlang
  r-testthat
  r-withr
  r-callr
  r-pkgload
  r-knitr
  r-ragg
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('64d96fee3845fd96d1eafaba37adf00e')
b2sums=('ea33c07a4c5c57ebdf4b715b17ee4c95cca9558dcfb4df80d0c606fd428cd592c708469c367293d134b8f91744bc7c267241d1844f344020582bee1afd4b12b4')

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
