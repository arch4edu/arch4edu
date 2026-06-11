# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=clubSandwich
_pkgver=0.6.1
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
  r-estimatr
  r-fixest
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
md5sums=('2256f1a1bd3887bb397cd69ac80ebd84')
b2sums=('ec0966fef8cd4a9078f2f12be02f0835169e1f5cc16c7dfc40e000820d683e1585c747e8c7a15fc9ecd5f72a61bbcb63225bd84e7ba39c20dad1c5da923070e1')

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
