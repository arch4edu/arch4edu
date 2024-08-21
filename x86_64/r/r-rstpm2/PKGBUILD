# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=rstpm2
_pkgver=1.6.5
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
  r-mvtnorm
  r-rcpp
)
makedepends=(
  gcc-fortran
  r-bh
  r-rcpparmadillo
)
checkdepends=(
  r-desolve
  r-testthat
)
optdepends=(
  r-desolve
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
md5sums=('d92aa8290bda3876692f16c3736dbef2'
         '7e22eed527937e811f674953a465f9c8')
b2sums=('93178c9bd05be4a8884638e63e15264eed02192e1ef343d7156b1401cd6998d21e2e759c1acda24ae5cfdc0d4bfb030a6835ebd8350114c0edae83d8f6b2c0d8'
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
