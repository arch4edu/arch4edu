# Maintainer: dhn <neilson+aur@sent.com>
# Maintainer: alhirzel
# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Filipe Laíns (FFY00) <lains@archlinux.org>
# Contributor: Ward Segers <w@rdsegers.be>
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=httr
_pkgver=1.4.8
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
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
md5sums=('8756015b94a9cff6f410ca4de8557f12')
b2sums=('e2f01d8c3ccee9a48cbc37c1331eed352573dd00faf0ae251ec87e81bb5c57afc7cf5182a29e2073d4208dc844aeec732b88eb35a6260461e978786e946caa2f')

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
