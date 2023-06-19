# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=progressr
_pkgver=0.13.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//[:-]/.}
pkgrel=5
pkgdesc="An Inclusive, Unifying API for Progress Updates"
arch=(any)
url="https://cran.r-project.org/package=${_pkgname}"
license=(GPL3)
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
md5sums=('48826c14b381db8d640665bf5bfb1135')
sha256sums=('0ffb3dcadde0cc191bad0ff9e05d000aa65e2fc339cfc94ebbb263088df5a4e1')

build() {
  mkdir -p build
  R CMD INSTALL "$_pkgname" -l build
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
