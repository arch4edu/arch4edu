# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=rstpm2
_pkgver=1.7.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Smooth Survival Models, Including Generalized Survival Models"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only OR GPL-3.0-only')
depends=(
  blas
  lapack
  r-bbmle
  r-fastghquad
  r-lsoda
  r-mvtnorm
  r-numderiv
  r-rcpp
)
makedepends=(
  gcc-fortran
  r-rcpparmadillo
)
checkdepends=(
  r-desolve
  r-testthat
)
optdepends=(
  r-eha
  r-flexsurv
  r-ggplot2
  r-mstate
  r-readstata13
  r-scales
  r-survpen
  r-testthat
  r-timereg
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz"
        "fix-tests.patch")
md5sums=('8bedc96bf5cdc727c195b9b8daf45d35'
         '7e22eed527937e811f674953a465f9c8')
b2sums=('b4a75454334527a181db62a0edfaaa74c78445349dfe19b94f2ebf249f97f025d59225377bc7d0247f5843145ac8db872302abfbcac40d702cefadf4faec797f'
        '61bb8ab4fff5514887b2fb678f461cc468c6f70388ddd1e21638fd73389a7d5481720a19f93f1ba55b40e59108efe3d92a8c14703ff9e984400ce50cbeec5d11')

prepare() {
  # skip failing tests
  patch -Np1 -i fix-tests.patch
}

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
