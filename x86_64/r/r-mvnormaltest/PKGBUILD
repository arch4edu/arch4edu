# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=mvnormalTest
_pkgver=1.0.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Powerful Tests for Multivariate Normality"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-copula
  r-moments
  r-nortest
)
optdepends=(
  r-knitr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('18d1f16b8894d68709dbfc21946268d1')
b2sums=('cf6f483da467fcffc092c7f4d2a3342a75bb41c1ada66b8a5084045122851a3825f3bc3a6aa2315e85e529d7ca3e67e57337991022263fc53422be0e9a92403a')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
