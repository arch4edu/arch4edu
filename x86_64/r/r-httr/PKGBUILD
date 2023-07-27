# Maintainer: dhn <neilson+aur@sent.com>
# Maintainer: alhirzel
# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Filipe Laíns (FFY00) <lains@archlinux.org>
# Contributor: Ward Segers <w@rdsegers.be>
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=httr
_pkgver=1.4.6
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="Tools for Working with URLs and HTTP"
arch=(any)
url="https://cran.r-project.org/package=${_pkgname}"
license=(MIT)
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
md5sums=('5c2b51eee477b9b8631877d68c4090c5')
sha256sums=('8d6d86cbef23738d2b4390490f7486d8cf7674f0a59c19f515f61cad35ec37b2')

build() {
  mkdir -p build
  R CMD INSTALL "$_pkgname" -l build
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
