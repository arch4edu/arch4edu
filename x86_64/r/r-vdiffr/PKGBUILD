# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: sukanka <su975853527@gmail.com>

_pkgname=vdiffr
_pkgver=1.0.9
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Visual Regression Testing and Graphical Diffing"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  libpng
  r-diffobj
  r-glue
  r-htmltools
  r-lifecycle
  r-rlang
  r-testthat
  r-xml2
)
makedepends=(
  r-cpp11
)
checkdepends=(
  r-ggplot2
)
optdepends=(
  r-covr
  r-decor
  r-ggplot2
  r-roxygen2
  r-withr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('9df7fa39cecf754417c06635fabcabf4')
b2sums=('fd8c4d21a8867accdff7e87d7f5282a230e1f7d1ae680723c4282455fad85981aec072691774d2c08b1d9683874da55200446e75bdc116352fa02f6d3a6201ff')

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
