# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=fixest
_pkgver=0.13.2
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Fast Fixed-Effects Estimations"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-only')
depends=(
  r-dreamerr
  r-numderiv
  r-rcpp
  r-sandwich
  r-stringmagic
)
checkdepends=(
  r-data.table
)
optdepends=(
  r-aer
  r-data.table
  r-emmeans
  r-estimability
  r-ggplot2
  r-knitr
  r-lfe
  r-pander
  r-pdftools
  r-plm
  r-rmarkdown
  r-tinytex
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('51669e0d09a29071a86b4937f7b98337')
b2sums=('ced8b6908066af323bc30bc2ef27c26369ddb887bd91fbc5cf47868bf137a1ee4391d276a1ecd34015916c66c2c0a8277f87dba75abacc0afae0808a94ce6032')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" Rscript --vanilla fixest_tests.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
