# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=rngWELL
_pkgver=0.10-9
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=3
pkgdesc="Toolbox for WELL Random Number Generators"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('BSD-3-Clause')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('30a683f8002c1aa17ca20be5ab1dcdb6')
b2sums=('62a5ef936a325fad9e8618880fbc8a0ab4e4860431d5e50c18d7538657a4de61492deab4f18c1eb8f070fb92a9305fc85325c7919f9210f5def86cafba34051c')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"

  install -d "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "/usr/lib/R/library/$_pkgname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"
}
