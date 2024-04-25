# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=fitdistrplus
_pkgver=1.1-11
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=5
pkgdesc="Help to Fit of a Parametric Distribution to Non-Censored or Censored Data"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r
)
optdepends=(
  r-actuar
  r-bookdown
  r-gamlss.dist
  r-generalizedhyperbolic
  r-ggplot2
  r-hmisc
  r-knitr
  r-mc2d
  r-rgenoud
  r-rmarkdown
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('512df42bc5b35be4690c17882315f33b')
b2sums=('a4fd884dcf7813d0fdd1c2c96dd4de6ca747b1e775553cdcc797006c45b6521395780193a8ff9c9258cad6d1eac00418dcdbcd557a6594407fbc734e97c45043')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
