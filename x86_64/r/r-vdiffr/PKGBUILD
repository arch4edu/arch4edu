# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: sukanka <su975853527@gmail.com>

_pkgname=vdiffr
_pkgver=1.0.8
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
md5sums=('d59ebff7b87afbc6defa2af55660fed5')
b2sums=('2dda8afb8f8256cf26c2ddd746de964b0d6c9ba2ca28b13d2d29c2b414a753cfe1e4129ef8ab4934dd7f7aa3924981263e08c9768beeafef69c0458cebe50029')

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
