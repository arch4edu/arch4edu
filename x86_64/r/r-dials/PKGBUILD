# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=dials
_pkgver=1.4.5
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Tools for Creating Tuning Parameter Values"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r-cli
  r-dicedesign
  r-dplyr
  r-glue
  r-hardhat
  r-lifecycle
  r-pillar
  r-purrr
  r-rlang
  r-scales
  r-sfd
  r-tibble
  r-tidyr
  r-tidyselect
  r-vctrs
  r-withr
)
checkdepends=(
  r-kernlab
  r-testthat
  r-xml2
)
optdepends=(
  r-covr
  r-ggplot2
  r-kernlab
  r-knitr
  r-rmarkdown
  r-testthat
  r-xml2
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('87a605298ab2a6b8828dcc67ea98b0c6')
b2sums=('cbf41aae148712417873199ee067692d4738ed9a5a59bed863f6e441998df3799f83b928ec770f0aa1f6de8333ac31d4995159a424711fc422976d18b083bcd7')

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

  install -d "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "/usr/lib/R/library/$_pkgname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"
}
