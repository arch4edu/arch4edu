# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: sukanka <su975853527@gmail.com>

_pkgname=onewaytests
_pkgver=3.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
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
  r-tibble
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('3adc7b0e56ef5dc3599c373eb165d9f4')
b2sums=('849a078fd007a5fbffc978964995bbffac5359660546c892224f1a90ccfaf684dda1ed0bc1b3a043c263ef9c383260b229544278164b7e14f5120e681fef4675')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
