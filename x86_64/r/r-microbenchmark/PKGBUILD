# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=microbenchmark
_pkgver=1.4.10
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=3
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
md5sums=('c64e467a01e792461a5cc544eac12f15')
b2sums=('458cb280410737719481b65b6bdd7281bf2c4d8320af55477f747c3b90c5f2d39c138b407ab2e64ea6a4dcafa3bdb6daa531a6a5fa94904dfe31672273f31a88')

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
