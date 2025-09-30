# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=modeldata
_pkgver=1.5.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Data Sets Useful for Modeling Examples"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r-dplyr
  r-purrr
  r-rlang
  r-tibble
  r-cli
)
checkdepends=(
  r-testthat
)
optdepends=(
  r-covr
  r-ggplot2
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('89e6ef8075ef1d8068bf0998b829548b')
b2sums=('741528c5bbf3ca7e5317b107b02897a6c01c6526c39c9bf131dffd97a88b7c5ab088689f213d6138272c9ecce344a82a379146d917a54685d053f9c2d2ee80e7')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" NOT_CRAN=true Rscript --vanilla testthat.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"

  install -d "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "/usr/lib/R/library/$_pkgname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"
}
