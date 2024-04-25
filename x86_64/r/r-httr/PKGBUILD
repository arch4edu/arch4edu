# Maintainer: dhn <neilson+aur@sent.com>
# Maintainer: alhirzel
# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Filipe Laíns (FFY00) <lains@archlinux.org>
# Contributor: Ward Segers <w@rdsegers.be>
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=httr
_pkgver=1.4.7
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="Tools for Working with URLs and HTTP"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r-curl
  r-jsonlite
  r-mime
  r-openssl
  r-r6
)
checkdepends=(
  r-httpuv
  r-testthat
)
optdepends=(
  r-covr
  r-httpuv
  r-jpeg
  r-knitr
  r-png
  r-readr
  r-rmarkdown
  r-testthat
  r-xml2
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('8965ffef86aea39922f435c019daf9fb')
b2sums=('85b4e8ebb549d09d4637b1cd339d070879e44d0e6e6f5743129806b7be430dc13deea36af9c1c716b591ea93b4e6953de4bf0caa9b5ee3d0253c17282ae0c538')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" Rscript --vanilla testthat.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"

  install -d "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "/usr/lib/R/library/$_pkgname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"
}
