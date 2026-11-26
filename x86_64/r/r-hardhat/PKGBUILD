# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=hardhat
_pkgver=1.4.4
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
md5sums=('db564571fcfa69fcebc2cacd2af69f10')
b2sums=('085bf536533129e5ce870b66d7783cb3f61b9e5579b42a94d4b22f7bcc1bafd7fa54f8cee93c1d18910b1af62a7cd70ee31e27c666f5fc4d91b0a5a6c51a4296')

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
