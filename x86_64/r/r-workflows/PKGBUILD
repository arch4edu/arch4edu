# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=workflows
_pkgver=1.1.4
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Modeling Workflows"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
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
md5sums=('6e78b96d1969bfd9f87c841a8a36464d')
b2sums=('2da077bdf6b6e3f66eccc7e43b62b6e4ef3f164a5a5bccf3726b4d9d254aeb37ef3af6217b076baa20944ce689fd6e83951685d07485fb4876615daa8c65c6e0')

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
