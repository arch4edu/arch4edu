# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=Rcsdp
_pkgver=0.1.57.5
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=3
pkgdesc="R Interface to the CSDP Semidefinite Programming Library"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('CPL-1.0')
depends=(
  blas
  lapack
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('dec4357fda5865cfabd9f4ad7bf74d76')
b2sums=('2ff445ed29b3f845bfc0d58bcaddaf2e2b1a314bdded2a137e59a0d920c23388a214f993af4592b4dee681bf0a86840d9fb36b648a88487d254e84187d76d7c8')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
