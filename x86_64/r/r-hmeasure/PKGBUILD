# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=hmeasure
_pkgver=1.0-2
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=8
pkgdesc="The H-Measure and Other Scalar Classification Performance Metrics"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r
)
optdepends=(
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('f9e5a09f8faea5967d0350639b5fdb6a')
b2sums=('7a1d57363246d70115d7e6ed04fea61f43ada8f7138945c57f2fc3e8b18736291f96693b581456f4c4c384850be47704399f02041249f6115373d2ad50b30424')

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
