# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=microbenchmark
_pkgver=1.5.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Accurate Timing Functions"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('BSD-2-Clause')
depends=(
  r
)
optdepends=(
  r-ggplot2
  r-multcomp
  r-runit
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('871b2a4cc43b463f636a78b225423bce')
b2sums=('1c3173235ce0c7b85268edddd1a10ad6ec5ada709114c2845e92c38ec17cd8b0777c8eb3d957a4c3e37699ee3b416b3b3650369d9fe7de77378ab805b8cebef2')

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
