# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: sukanka <su975853527@gmail.com>

_pkgname=heplots
_pkgver=1.7.8
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Visualizing Hypothesis Tests in Multivariate Linear Models"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-broom
  r-car
  r-magrittr
  r-purrr
  r-rgl
  r-tibble
)
optdepends=(
  r-animation
  r-archdata
  r-bookdown
  r-candisc
  r-cardata
  r-corrgram
  r-dplyr
  r-effects
  r-ggplot2
  r-glue
  r-gplots
  r-here
  r-knitr
  r-mvinfluence
  r-patchwork
  r-qqtest
  r-reshape
  r-reshape2
  r-rmarkdown
  r-robustbase
  r-rrcov
  r-sleuth2
  r-tidyr
  r-tinytable
  r-markdown
  r-vcdextra
  r-r.rsp
  r-litedown
  r-aplpack
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('1cac55edc083ba2346c9ac7ce8c1cb12')
b2sums=('e928fb78af6398678a5058657d9a24af926c8d952b99079c929cdad344d7e5635b3792259cef58ceb0e2d68543cd5e014e54664e3375683e42c604dd867018a7')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
