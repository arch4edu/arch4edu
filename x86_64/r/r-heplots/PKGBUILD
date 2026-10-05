# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: sukanka <su975853527@gmail.com>

_pkgname=heplots
_pkgver=1.8.6
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Visualizing Hypothesis Tests in Multivariate Linear Models"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-car
  r-generics
  r-glue
  r-magrittr
  r-purrr
  r-rgl
  r-tibble
)
optdepends=(
  r-animation
  r-aplpack
  r-archdata
  r-bookdown
  r-broom
  r-candisc
  r-cardata
  r-corrgram
  r-dplyr
  r-effects
  r-effectsize
  r-ggbiplot
  r-ggplot2
  r-gplots
  r-here
  r-htmltools
  r-knitr
  r-litedown
  r-lmtest
  r-markdown
  r-mvinfluence
  r-parameters
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
  r-vcdextra
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('a2d4beb4e52bd204f5a0539a438060d7')
b2sums=('a92f7a8e3455923f52c4fea25f7b9c7bc3f2583afa736b49257869aba1a78fbeb0faa21867b12ce70d6c5d9716fb15317f48942936b6d1d3b71d243c7746c568')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
