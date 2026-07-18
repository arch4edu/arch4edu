# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Taekyung Kim <Taekyung.Kim.Maths@gmail.com>

_pkgname=lme4
_pkgver=2.0-6
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
  r-rdpack
  r-reformulas
)
makedepends=(
  r-rcpp
  r-rcppeigen
)
optdepends=(
  r-car
  r-dfoptim
  r-dharma
  r-future.apply
  r-gamm4
  r-ggplot2
  r-glmmtmb
  r-gridextra
  r-hsaur3
  r-knitr
  r-memss
  r-merderiv
  r-mlmrev
  r-numderiv
  r-optimx
  r-pbkrtest
  r-performance
  r-rmarkdown
  r-rr2
  r-see
  r-semeff
  r-statmod
  r-testthat
  r-tibble
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('cf60da58c196ac7f2ac8094b6a13b6ce')
b2sums=('9c483d8a68c11940188e4080fa8ac06506b0d3b3675be430b5c693c2bfe51123659ff45ef03006a7ff357e11c6761a9dd149bfecf538dc68973344b8bc276eab')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
