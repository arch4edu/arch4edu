# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: sukanka <su975853527@gmail.com>

_pkgname=heplots
_pkgver=1.8.7
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
md5sums=('7491ba35ac8c3ef07e4782e3ae781abe')
b2sums=('3c8550d09a9673bed34ec2e7f8449c3668bd7fe9b120dbb7e29f5a3117f80e715b200e2a043dd0e7d2d6f371c30d3d3b1b745d2bef834c4a989afec5ac16868a')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
