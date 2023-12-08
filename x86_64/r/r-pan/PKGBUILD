# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=pan
_pkgver=1.9
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
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
md5sums=('b6c1c18a3f9b89f068878e065b1f00a4')
sha256sums=('cd91232d653783ea7f34c0eebaa80c472b5501b21eea500c4c1a8e57116c6eea')

build() {
  mkdir -p build
  R CMD INSTALL "$_pkgname" -l build
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
