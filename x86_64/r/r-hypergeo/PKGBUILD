# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=hypergeo
_pkgver=1.2-14
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="The Gauss Hypergeometric Function"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  r-contfrac
  r-desolve
  r-elliptic
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('a4abecbbe6732d20d251ac9bc6d466ff')
b2sums=('d18328c1c29c1a178b8d3682e45425a1b1fce22fcda3b81fef1d6d920c9a8c2a3802265186ace0b8105f389b5b1f3e2faa9281718f9d24c4cf4ebcc449b07669')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
