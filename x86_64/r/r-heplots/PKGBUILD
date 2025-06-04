# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: sukanka <su975853527@gmail.com>

_pkgname=heplots
_pkgver=1.7.5
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
md5sums=('060d6ae5af2f6aab7d21bc337f7b70f6')
b2sums=('ac229e2b97e83ed7eeabb0c1810cbe781f98989c05ecc8e6cd18d08763cebbfc31e33fead53803a2fe0afa34a90e79584edbae687ed7fc50a070f1563a8e9b8d')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
