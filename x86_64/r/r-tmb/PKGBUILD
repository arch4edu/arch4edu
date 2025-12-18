# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=TMB
_pkgver=1.9.19
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Template Model Builder: A General Random Effect Tool Inspired by 'ADMB'"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  blas
  lapack
  r
)
makedepends=(
  r-rcppeigen
)
optdepends=(
  r-numderiv
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('24e1ffd4e211720131f46a7ecc0e03ee')
b2sums=('aeff49948935f4e72882e248c141d8078720f6dee68730cf25d2dc21ca3013562bdabe2fdf2448d6371cc0de6197f0ed2a442da1ad75854b104b088c7c9ed5d7')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
