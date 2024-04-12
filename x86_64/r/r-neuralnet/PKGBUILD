# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=neuralnet
_pkgver=1.44.2
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=8
pkgdesc="Training of Neural Networks"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-deriv
)
optdepends=(
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('9ac984dd54ed1c3f68a501c7b2c7c014')
b2sums=('a28d54c21af1a77e2b9863b7e3acd82069da0bf7623b55b42602d86078a33721c49b240792766b3ec737401aaaae281336fb541d9e98a4a84e9fbbdf76ba2bdf')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
