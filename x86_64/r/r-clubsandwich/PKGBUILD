# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=clubSandwich
_pkgver=0.7.0
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
  r-mmrm
  r-plm
  r-rmarkdown
  r-robumeta
  r-testthat
  r-zoo
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('08f806bfdb8a5117a8aabaaf6264eb52')
b2sums=('93e2ba97708cbde8d3c3e33bde8840009a27ce8f0bae87a4ddf90bc00195b08bf55831bb462dfda89e8a40ecda635c00d0554b434528be90c9427db7d4969704')

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
