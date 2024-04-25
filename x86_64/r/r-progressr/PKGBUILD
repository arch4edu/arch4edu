# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=progressr
_pkgver=0.14.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=3
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
  r-pbmcapply
  r-plyr
  r-progress
  r-purrr
  r-rpushbullet
  r-rstudioapi
  r-shiny
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('553ed3dd68689ea70694f2672fa3766a')
b2sums=('904cac728a9ba594eb1cfda98b1cb498addc87dffdad5baf3aa64ba44e25ccbf4117b442f1d304b5753c3f3aefc1b2671aa89687542432279948f2f890c9a8cc')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
