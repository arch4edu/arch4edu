# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=clubSandwich
_pkgver=0.6.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Cluster-Robust (Sandwich) Variance Estimators with Small-Sample Corrections"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-only')
depends=(
  r-lifecycle
  r-sandwich
)
checkdepends=(
  r-aer
  r-cardata
  r-geepack
  r-ivreg
  r-lme4
  r-metadat
  r-metafor
  r-mlmrev
  r-plm
  r-robumeta
  r-testthat
)
optdepends=(
  r-aer
  r-cardata
  r-covr
  r-formula
  r-geepack
  r-ivreg
  r-knitr
  r-lme4
  r-metadat
  r-metafor
  r-mlmrev
  r-plm
  r-rmarkdown
  r-robumeta
  r-testthat
  r-zoo
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('735089f5126a48f6c0951c065f920e0b')
b2sums=('9cf86d3b275afdb2db6140cbc0d2e7b473d71ffa4d5bcff65fb932cb267450be0c72534348857b507413f3c8814eef4d7b3541a44f8e9c3330955470d68fa790')

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
}
