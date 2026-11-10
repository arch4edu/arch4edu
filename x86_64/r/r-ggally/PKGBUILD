# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=GGally
_pkgver=2.5.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Extension to 'ggplot2'"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-cli
  r-dplyr
  r-ggplot2
  r-ggstats
  r-gtable
  r-lifecycle
  r-magrittr
  r-progress
  r-rcolorbrewer
  r-rlang
  r-s7
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
  r-airports
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
  r-scagnostics
  r-sna
  r-spelling
  r-testthat
  r-vdiffr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('2f147baec8f9568d38caf83e822808b2')
b2sums=('b267476eeb92a49682167f3993e18d5e3f2e54f141a311e93e4ab7961010d9ff15c87b8d40de4d2cb5edec13839d2cdf99714c16c5f1026036f1db09a082b1c2')

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
