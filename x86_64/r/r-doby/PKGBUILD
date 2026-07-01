# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=doBy
_pkgver=4.7.2
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
  r-forecast
  r-ggplot2
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
  r-microbenchmark
  r-multcomp
  r-pbkrtest
  r-rmarkdown
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('24e2764844cfed461a0cd032f9de71ed')
b2sums=('3eca860804aba49926d78a39c83a457490cd63d6078430a71f271071ac7ae6171a24aab1a1dcfbf6d27ba69893e4634867939d14f6ab71c514c39e4ec9c7d53d')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
