# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: sukanka <su975853527@gmail.com>

_pkgname=heplots
_pkgver=1.8.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
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
  r-effectsize
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
md5sums=('f93c63368cc1ebc8c601bc4d8426db16')
b2sums=('de1f47944d1058ae5faf7372bdae9bfd2ffaca1fa494e9b6ec76a71ef8acf145f0a0a3da847563da1665ca1038cf1a2232da21854d62636b6604f5882ede7319')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
