# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=Boom
_pkgver=0.9.16
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Bayesian Object Oriented Modeling"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('LGPL-2.1-only')
depends=(
  r
)
optdepends=(
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('d3a299c3c467a7075d762562028b3907')
b2sums=('ecf95c302dbf32b316be59178db2db29e75692fc0ae5469325838ad2bafedec9a323827127869061407254b9d308fc417d19709b02f159a3cfb11fe13e872d23')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
