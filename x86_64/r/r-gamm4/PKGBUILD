# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=gamm4
_pkgver=0.3-0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Generalized Additive Mixed Models using 'mgcv' and 'lme4'"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-lme4
)
optdepends=(
  r-reticulate
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('c7e564cd312013f12776df9714e0ba5c')
b2sums=('c0fa2269c406eea1e0ce62cc626ddda8f892c46f761f2d6e1d76de74c67e48f1de50f40005435e12be6b4cd5defc740624c63d3809e744d77c0a5096ecbcaae9')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
