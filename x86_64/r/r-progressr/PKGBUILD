# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=progressr
_pkgver=0.17.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="An Inclusive, Unifying API for Progress Updates"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-or-later')
depends=(
  r-digest
)
optdepends=(
  r-base64enc
  r-beepr
  r-cli
  r-commonmark
  r-crayon
  r-dofuture
  r-foreach
  r-furrr
  r-future
  r-future.apply
  r-ntfy
  r-pbmcapply
  r-plyr
  r-progress
  r-purrr
  r-rpushbullet
  r-rstudioapi
  r-shiny
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('d214d86f22affc7f970b218b11dab681')
b2sums=('76b7c2d25323ed947eaa9cb620b0c12591f2bec38cd59efc5fe5b7ecfcf0aad24586819903d52444acb3e55b654b597c3d2ca9859bfb2711f65fe80bb1a1d7e8')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
