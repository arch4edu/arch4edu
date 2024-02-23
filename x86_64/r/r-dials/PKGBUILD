# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=dials
_pkgver=1.2.1
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
  r-kernlab
  r-knitr
  r-rmarkdown
  r-testthat
  r-xml2
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('71af0aae8351ff80de1e3d8c55f5c135')
b2sums=('2763d0e81b810fc632f7396fd6b41324553e11180cf8293743201652f8915b0fdedca3c657bde6bff7cbeb0b93f5299990de431b32eeddecbc66b92491bc9d41')

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
