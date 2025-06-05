# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=mvShapiroTest
_pkgver=1.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=3
pkgdesc="Generalized Shapiro-Wilk test for multivariate normality"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-or-later')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('b0098814d73d98b7d66a3eb3932e30f0')
b2sums=('2dddf986886b03aae634f3350a8f03a787a1e794a64878651b7e3fa4610945a7def44266494153131a8226a5758d881738bbdd0f88f06f3766abf61d08433071')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
