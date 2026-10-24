# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Taekyung Kim <Taekyung.Kim.Maths@gmail.com>

_pkgname=lme4
_pkgver=2.1-0
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
md5sums=('673b4943af202f4ea2fec10aa92732eb')
b2sums=('79f81406181f925283ec3096a91091360f081a04397b30c9f37ff95e6bc4d48ac206330b82533c86dd4bfcadd1e03ff561bc3845f7262f8e5ec57c928ee6e2e0')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
