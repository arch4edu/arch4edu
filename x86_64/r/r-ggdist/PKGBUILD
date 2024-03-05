# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=ggdist
_pkgver=3.3.2
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Visualizations of Distributions and Uncertainty"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-or-later')
depends=(
  r-cli
  r-distributional
  r-ggplot2
  r-glue
  r-gtable
  r-numderiv
  r-quadprog
  r-rcpp
  r-rlang
  r-scales
  r-tibble
  r-vctrs
  r-withr
)
checkdepends=(
  r-beeswarm
  r-fda
  r-fontquiver
  r-mvtnorm
  r-posterior
  r-showtext
  r-svglite
  r-sysfonts
  r-testthat
  r-tidyr
  r-vdiffr
)
optdepends=(
  r-beeswarm
  r-broom
  r-covr
  r-dplyr
  r-fda
  r-fontquiver
  r-knitr
  r-mvtnorm
  r-patchwork
  r-pkgdown
  r-posterior
  r-ragg
  r-rmarkdown
  r-showtext
  r-svglite
  r-sysfonts
  r-testthat
  r-tidyr
  r-tidyselect
  r-vdiffr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('4272ed3112d6770ed3bea3697eea180e')
b2sums=('efbf4e460afcfc5092a8b8eba4bbfdab1dd55da087a9124ac3093e19a1505a6debd0b218ba607e251f4c5aadf68223800f555518c2b556cd59703030bcffe386')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" NOT_CRAN=true Rscript --vanilla testthat.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
