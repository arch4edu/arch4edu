# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=statnet.common
_pkgver=4.11.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Common R Scripts and Utilities Used by the Statnet Project Software"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-only')
depends=(
  r-coda
)
optdepends=(
  r-covr
  r-rlang
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('69d37cc27d33b8d3bc1c7d9b2672fce5')
b2sums=('ed6a3c2f2653e34f0cf8223ba07527cfff7247fb85324ec1f39c6e28bfb723ff4dcb7fccd1ea906bc3ecfb580c72bc50062cfeb704860644867ff444d8fd76c3')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
