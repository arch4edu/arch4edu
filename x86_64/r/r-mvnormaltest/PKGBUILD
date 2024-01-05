# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=mvnormalTest
_pkgver=1.0.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Powerful Tests for Multivariate Normality"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=(GPL)
depends=(
  r-copula
  r-moments
  r-nortest
)
optdepends=(
  r-knitr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('f3525fd9bd8d908ba0b2201a3f147039')
b2sums=('66e8dd404ea7e16f42e286f5432ec9993f4fade45795823258e81087b7f2fe048b2b94ec650a61d7ee9453689f2fad916b412416d081ba07186ec042b884ac8b')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
