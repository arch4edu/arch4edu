# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=hardhat
_pkgver=1.4.3
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Construct Modeling Packages"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r-cli
  r-glue
  r-rlang
  r-tibble
  r-vctrs
  r-sparsevctrs
)
optdepends=(
  r-covr
  r-crayon
  r-devtools
  r-knitr
  r-modeldata
  r-recipes
  r-rmarkdown
  r-roxygen2
  r-testthat
  r-usethis
  r-withr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('a6365cb2e5a5b4dc8b6c0c6e583b333e')
b2sums=('f8e70f2846fcfbb338d6661e98326dceea2709d51111644513906cf67a0ff5e0e5eda6526de9c3169d87b48d0deb3e5f49ff0fde6550781be8a546937245bf90')

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
