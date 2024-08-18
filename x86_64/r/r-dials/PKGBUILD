# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=dials
_pkgver=1.3.0
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
md5sums=('585072b9d580ddd916386a7ba5a62afe')
b2sums=('ef7fd6b12573ea7818949c3536e37caec1a53565912632d110047a0717a5ccc02ef25edaed3418a59260eeff7cf2c6c3a19cfa27849a499193473c656394b670')

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
