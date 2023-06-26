# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=pan
_pkgver=1.8
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Multiple Imputation for Multivariate Panel or Clustered Data"
arch=(x86_64)
url="https://cran.r-project.org/package=${_pkgname}"
license=(GPL3)
depends=(
  r
)
makedepends=(
  gcc-fortran
)
optdepends=(
  r-lme4
  r-mitools
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('2915c6196eaa2eaff77cb3e3a1489ba8')
sha256sums=('d1a77a02c158a4a10e913024d5019cf078cb0ff636c923e5e3e93e10643113ee')

build() {
  mkdir -p build
  R CMD INSTALL "$_pkgname" -l build
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
