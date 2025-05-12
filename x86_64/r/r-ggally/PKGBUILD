# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=GGally
_pkgver=2.2.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=3
pkgdesc="Extension to 'ggplot2'"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-dplyr
  r-ggplot2
  r-ggstats
  r-gtable
  r-lifecycle
  r-magrittr
  r-plyr
  r-progress
  r-rcolorbrewer
  r-rlang
  r-scales
  r-tidyr
)
checkdepends=(
  r-chemometrics
  r-crosstalk
  r-geosphere
  r-ggforce
  r-hmisc
  r-intergraph
  r-mapproj
  r-maps
  r-network
  r-sna
  r-testthat
  r-vdiffr
)
optdepends=(
  r-broom
  r-broom.helpers
  r-chemometrics
  r-crosstalk
  r-emmeans
  r-geosphere
  r-ggforce
  r-hmisc
  r-igraph
  r-intergraph
  r-knitr
  r-labelled
  r-mapproj
  r-maps
  r-network
  r-rmarkdown
  r-roxygen2
  r-scagnostics
  r-sna
  r-spelling
  r-testthat
  r-vdiffr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('9acff4b4e2fd3197ac98fada1266434a')
b2sums=('20f2e5ff8a7c002e509641f7248a140a6a738bf11c68215bd38f04c701e195b98ac738607a42d9dbcc3ad55e3cf7565549d9b3e5a6d68166149c3f557db116f1')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

_check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" NOT_CRAN=true Rscript --vanilla testthat.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
