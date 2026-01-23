# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=fitdistrplus
_pkgver=1.2-5
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Help to Fit of a Parametric Distribution to Non-Censored or Censored Data"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-rlang
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
md5sums=('2cc7195f1d2d1eb5a302bbc737912892')
b2sums=('22bdcc8c8b6a2728b2d0aeb2150a5a4b5eee03ddb6e25168a0d1e9633db213eaafde6f0b660bf410fbe75082b556e1990f6d21c500dc2271f5e7dbc2d370bd30')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
