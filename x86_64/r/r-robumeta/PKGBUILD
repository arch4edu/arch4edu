# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=robumeta
_pkgver=2.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=3
pkgdesc="Robust Variance Meta-Regression"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  r
)
optdepends=(
  r-clubsandwich
  r-r.rsp
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('8f80a79fc262c49172df2bcf78e3e1e3')
b2sums=('52e6db9eeb466b4fe7c9910f21f5980c54de7e970e439eeab3c91c02072587db8721cd346bd7f87e5ddf26e5501eefd81d5801dd9b32332fce3dbd4e27ae4abc')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
