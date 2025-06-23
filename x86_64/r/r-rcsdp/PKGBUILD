# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=Rcsdp
_pkgver=0.1.57.6
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
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
md5sums=('aecd9329a335081841e2724252e29241')
b2sums=('23ca53c23a1c754dbae142c4985da534e2a453ca4044e317009b43d38aaf2bf674f8752b199103574b4792aace2e028904978eaf84fb73a6a11bf75bbc4df592')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
