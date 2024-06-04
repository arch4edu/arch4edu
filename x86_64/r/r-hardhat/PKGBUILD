# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=hardhat
_pkgver=1.4.0
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
md5sums=('944be6ebd162bb6fce66496c1a6f063f')
b2sums=('d7c648bde6d6f7d1c0cb3422509de8f12f9e2eb991af14a3f47db9919c588b5beeb2673f673ce3496539d9486f8bb0dc1c23b2b683c70c22bce21105631ee6d7')

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
