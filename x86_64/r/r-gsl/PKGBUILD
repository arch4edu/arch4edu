# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=gsl
_pkgver=2.1-9
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Wrapper for the Gnu Scientific Library"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-only')
depends=(
  gsl
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('ba064d2fc03ed6116cd46e55fb11ac84')
b2sums=('c957ee08a5876c4b94b3b18038c314660bf81f02633f6269b72d3f2efc7b364ef79aa4723d576a6f5c497345029465bc8b19d7f84de92b683f5ea01cc23efd8c')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
