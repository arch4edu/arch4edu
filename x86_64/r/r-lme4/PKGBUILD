# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Taekyung Kim <Taekyung.Kim.Maths@gmail.com>

_pkgname=lme4
_pkgver=2.0-1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Linear Mixed-Effects Models using 'Eigen' and S4"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-rdpack
  r-minqa
  r-nloptr
  r-reformulas
  r-rlang
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
  r-glmmtmb
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
md5sums=('e90aec2abcdc6919bf1041d968416b01')
b2sums=('cd96c89668879e6ccc4a27b364253222a487f881d43fba2688de466058f52908feb92264891a56723d1146ae00fc38fbabcefcc0bc4bbd574eaf09eea7d736ce')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
