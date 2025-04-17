# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=doBy
_pkgver=4.6.26
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Groupwise Statistics, LSmeans, Linear Estimates, Utilities"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-broom
  r-cowplot
  r-deriv
  r-dplyr
  r-ggplot2
  r-microbenchmark
  r-modelr
  r-rlang
  r-tibble
  r-tidyr
)
optdepends=(
  r-geepack
  r-knitr
  r-lme4
  r-markdown
  r-multcomp
  r-pbkrtest
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('5fa4577b2e6a90acf64a60bc9535915b')
b2sums=('1ead718905141fc8d596c9d6211f9b61de13de01520f3a57dc67b6667b615e533b269dcf599d4e4d437d0eaaaf89a78d60cf0e2892b2903790e1b436410dde11')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
