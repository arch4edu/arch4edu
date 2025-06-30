# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=doBy
_pkgver=4.7.0
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
md5sums=('368755bfed56596607935c4bc91ebc67')
b2sums=('09cfdaf40917f4d25e71b4052a122818f7f1c2b6da4181f8f27936201439585d52de71a0eb33cc94e1c054b17b1bf408e40bd0536c68e8776b0a555356b70aff')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
