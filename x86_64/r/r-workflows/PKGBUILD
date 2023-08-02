# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=workflows
_pkgver=1.1.3
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Modeling Workflows"
arch=(any)
url="https://cran.r-project.org/package=${_pkgname}"
license=(MIT)
depends=(
  r-cli
  r-generics
  r-glue
  r-hardhat
  r-lifecycle
  r-modelenv
  r-parsnip
  r-rlang
  r-tidyselect
  r-vctrs
)
optdepends=(
  r-butcher
  r-covr
  r-dials
  r-knitr
  r-magrittr
  r-modeldata
  r-recipes
  r-rmarkdown
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('d646ec2abe7014fa31ccf569139dbf4c')
sha256sums=('baa26a876b56e61bd3339a44297e3c5b719a92c9316495fb17836dfa8caf4181')

build() {
  mkdir -p build
  R CMD INSTALL "$_pkgname" -l build
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"

  install -d "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "/usr/lib/R/library/$_pkgname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"
}
