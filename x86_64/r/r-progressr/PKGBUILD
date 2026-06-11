# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=progressr
_pkgver=0.19.0
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
md5sums=('cd86a7e4e49895077b89b81833996487')
b2sums=('bb7afa79a935d57ea8fc6d7cd9f1e5d15381399c89cffb6ff7af403066ab78ed2d0a91a841e46784a1f5d75d9951a234711ec2edfcc6a6a21665e87b54f343a0')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
