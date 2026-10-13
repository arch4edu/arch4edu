# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: sukanka <su975853527@gmail.com>

_pkgname=onewaytests
_pkgver=3.2
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="One-Way Tests in Independent Groups Designs"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-car
  r-ggplot2
  r-moments
  r-nortest
  r-wesanderson
)
optdepends=(
  r-aid
  r-testthat
  r-tibble
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('23f3e8f82a529f87ccfd5190c3d63ad2')
b2sums=('aa25498a50139771a17c27496f2f302fd985b807f8a0022474d99c210cbe684d0a11b778367bb74d9ab654674a74b6ec2ff5cdb0ad1db6b9909a32be20e5af95')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
