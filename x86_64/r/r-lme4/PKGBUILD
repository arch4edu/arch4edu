# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Taekyung Kim <Taekyung.Kim.Maths@gmail.com>

_pkgname=lme4
_pkgver=1.1-37
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Linear Mixed-Effects Models using 'Eigen' and S4"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-minqa
  r-nloptr
  r-reformulas
)
makedepends=(
  r-rcpp
  r-rcppeigen
)
optdepends=(
  r-car
  r-dfoptim
  r-gamm4
  r-ggplot2
  r-hsaur3
  r-knitr
  r-memss
  r-merderiv
  r-mlmrev
  r-numderiv
  r-optimx
  r-pbkrtest
  r-rmarkdown
  r-rr2
  r-semeff
  r-statmod
  r-testthat
  r-tibble
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('b271a47af88be12780d009b941afb84e')
b2sums=('b3a20735963389b89da2525d51ce731f1a8d957ca0e223322c0a33dbad4ba3d25d508f9ab03b7ed5d40e8dafc3ca5da94492d713aea924b97d629798d133faec')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
