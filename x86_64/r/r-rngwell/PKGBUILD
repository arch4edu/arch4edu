# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=rngWELL
_pkgver=0.10-10
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Toolbox for WELL Random Number Generators"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('BSD-3-Clause')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('5344e2d874138556d0a3b0981b6a613e')
b2sums=('75d35a577627dbd6107d32f8551a498d7c81815436e5f939a02323b3d5e08a6fe56a24e9e9da84effc3b433047359c67cea454c6d2933a04b7356c489550aeb9')

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
