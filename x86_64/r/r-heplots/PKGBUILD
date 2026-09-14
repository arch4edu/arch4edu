# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: sukanka <su975853527@gmail.com>

_pkgname=heplots
_pkgver=1.8.5
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
  r-glue
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
md5sums=('b115b4d28c34cc15ebc1f90114d029b5')
b2sums=('6747bfd442128b950d1e12079603d7d78c387ddeca4c3a2b80b21ee7990867819b8d61e2843e3b4331c7531947d11e3a6d0e1791053e7400e0c0cff47b4346b3')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
