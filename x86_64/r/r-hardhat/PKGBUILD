# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=hardhat
_pkgver=1.4.2
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
md5sums=('b14889116413fdf702b95c488cb52f66')
b2sums=('1052efd7e45c6c6cc8aff92217111f1c89c3a0ddd5e9bf81794788414ccb8e62238b5da770a2559df24b037e8d1e637ad77be6524bfa9dc174056f6a5aceddf6')

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
