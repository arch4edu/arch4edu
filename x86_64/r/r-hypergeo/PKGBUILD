# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=hypergeo
_pkgver=1.2-13
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=7
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
md5sums=('fe7a150c10ab854fa5f6d70ee0f7549e')
b2sums=('8fec028c73b04b531d294c247081ab707ae7c1df3f2638d2996fe4c5dfb776a8109900db0d5473fb04a5aa959b2fee7ed0f6832e0f298bb0c447de0af2847c1d')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
