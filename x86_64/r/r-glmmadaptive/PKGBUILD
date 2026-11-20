# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=GLMMadaptive
_pkgver=0.9-9
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
md5sums=('729ca1ccb062ad13a6e4e09b34cd683d')
b2sums=('ea0f3bb7756275883bdcc056db0bf7be892e4a73a7fa196f9e3e2dc99b644df8b626becfe6335082aec4e71b9d1ee751e7bea2b92a891ac61480b06366df1d95')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
