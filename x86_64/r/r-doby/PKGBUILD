# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=doBy
_pkgver=4.7.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="Groupwise Statistics, LSmeans, Linear Estimates, Utilities"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-broom
  r-cowplot
  r-deriv
  r-dplyr
  r-forecast
  r-ggplot2
  r-microbenchmark
  r-modelr
  r-purrr
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
  r-rmarkdown
  r-pbkrtest
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('095081ddc08b5324ab5999af1a9339fb')
b2sums=('ba87f1194eb4bb4638ec3c50342901e78c54782a3c255b538add5515c96945cfda9bbe81386651277c884ae5e9960ef84e79513fb2f8b48087b231ff513b32eb')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
