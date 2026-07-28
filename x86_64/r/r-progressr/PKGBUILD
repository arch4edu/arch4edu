# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=progressr
_pkgver=1.0.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="An Inclusive, Unifying API for Progress Updates"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('Apache')
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
md5sums=('c3672e20ef7ae91d8c14eedbf6e0a5a3')
b2sums=('c30acc5fa5881436fca41f18648cf075574e8302f6cbc06dbd69d56ca0ca0b30f34e9f92878e779a6e208735c025448a54253252c11a6024b1aa9429f84a49d9')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
