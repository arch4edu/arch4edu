# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=ggh4x
_pkgver=0.3.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Hacks for 'ggplot2'"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r-cli
  r-ggplot2
  r-gtable
  r-lifecycle
  r-rlang
  r-scales
  r-vctrs
  r-s7
)
checkdepends=(
  r-fitdistrplus
  r-ggdendro
  r-testthat
  r-vdiffr
)
optdepends=(
  r-covr
  r-fitdistrplus
  r-ggdendro
  r-knitr
  r-rmarkdown
  r-testthat
  r-vdiffr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('2de953548f9336e1af67de6012f62477')
b2sums=('e54ddaa4d059975d74f6fefec2341a06de92055be0aeb9160dc06f14ab39c91e843623cc55cf7aba482ffda8ffdc1eaa767552756f3414bfe4c03b46d0eb157c')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

#check() {
#  cd "$_pkgname/tests"
#  R_LIBS="$srcdir/build" NOT_CRAN=true Rscript --vanilla testthat.R
#}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"

  install -d "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "/usr/lib/R/library/$_pkgname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"
}
