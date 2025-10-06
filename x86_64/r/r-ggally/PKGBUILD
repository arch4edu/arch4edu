# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=GGally
_pkgver=2.4.0
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
md5sums=('10e743f036dd7a85cc00e5d726c35df5')
b2sums=('0ebbcf104689a5f965f05e2f252ffcc0c347894db53ff0c619ea13c9738a3bff11241ecf1dbb163452e58b3d2fbcf1536c80fcb727c33b1487643c83ab6c0da8')

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
