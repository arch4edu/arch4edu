# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=GLMMadaptive
_pkgver=0.9-7
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Generalized Linear Mixed Models using Adaptive Gaussian Quadrature"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-or-later')
depends=(
  r-matrixstats
)
optdepends=(
  r-dharma
  r-effects
  r-emmeans
  r-estimability
  r-knitr
  r-multcomp
  r-optimparallel
  r-pkgdown
  r-rmarkdown
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('321a078158c71c7de29dad618c94823b')
b2sums=('2a3f7e8fd792f9b67e5f67522db6069fb9511ba601e9fe8a2473c24865681e7026a04775e03052e8547fee4602a5dec2906f5b254cdb6573a4b89398b57db2fd')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
