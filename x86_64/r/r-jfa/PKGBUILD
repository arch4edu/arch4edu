# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: sukanka <su975853527@gmail.com>

_pkgname=jfa
_pkgver=0.7.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=4
pkgdesc="Statistical Methods for Auditing"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=(GPL3)
depends=(
  r-bde
  r-extradistr
  r-ggplot2
  r-rcpp
  r-rcppparallel
  r-rstan
  r-rstantools
  r-truncdist
)
makedepends=(
  r-bh
  r-rcppeigen
  r-stanheaders
)
checkdepends=(
  r-benford.analysis
  r-benfordtests
  r-beyondbenford
  r-fairness
  r-mus
  r-rmarkdown
  r-samplingbook
  r-testthat
)
optdepends=(
  r-benford.analysis
  r-benfordtests
  r-beyondbenford
  r-fairness
  r-kableextra
  r-knitr
  r-mus
  r-rmarkdown
  r-samplingbook
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('cf512f96cfd13b56fab2669a34fb3aaf')
b2sums=('b72eb1a9e20b382c7c0c81b85881c3c13e9c14720f3ab2b9600baebd5831e9dd47e0a5697df1ddf0e6ccbe1b71538cdc688c20dff2da665e5dc77722f7e401f5')

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
