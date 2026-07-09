# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Kibouo <csonka.mihaly@hotmail.com>
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=xfun
_pkgver=0.60
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Supporting Functions for Packages Maintained by 'Yihui Xie'"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r
)
checkdepends=(
  r-testit
)
optdepends=(
  r-commonmark
  r-curl
  r-data.table
  r-jsonlite
  r-knitr
  r-litedown
  r-magick
  r-mime
  r-pak
  r-qs2
  r-remotes
  r-rstudioapi
  r-testit
  r-tinytex
  r-xml2
  r-yaml
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('1bea9ab58602d9b6eac3b5823a95e5e6')
b2sums=('56670d6972d0529df41af2d15bb9b26ecb70695b16876e72afd3e089c29f377ead7a5672c30932fe80f0b3f971df8dddc8417afcf14e156c21e146f4f3269942')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" _R_CHECK_PACKAGE_NAME_=false Rscript --vanilla test-all.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"

  install -d "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "/usr/lib/R/library/$_pkgname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"
}
