# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=pan
_pkgver=1.6
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//[:-]/.}
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
md5sums=('86525839b38e045d2577eaf045269415')
sha256sums=('adc0df816ae38bc188bce0aef3aeb71d19c0fc26e063107eeee71a81a49463b6')

build() {
  mkdir -p build
  R CMD INSTALL "$_pkgname" -l build
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
