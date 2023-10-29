# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: sukanka <su975853527@gmail.com>

_pkgname=onewaytests
_pkgver=3.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="One-Way Tests in Independent Groups Designs"
arch=(any)
url="https://cran.r-project.org/package=${_pkgname}"
license=(GPL)
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
sha256sums=('67836ba322b457c45dd637d0ee08b0a95f61be00cd7e149d1eb2dd64d07bbf62')

build() {
  mkdir -p build
  R CMD INSTALL "$_pkgname" -l build
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
