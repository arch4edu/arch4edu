# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=DRR
_pkgver=0.0.4
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=3
pkgdesc="Dimensionality Reduction via Regression"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-only')
depends=(
  r-cvst
  r-kernlab
)
optdepends=(
  r-knitr
  r-rmarkdown
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('54da2f97bd8b0dd57137f98523c3fa0a')
b2sums=('d28e1e3a8bb13369318dca0913ecdac374bbaddd88ffe1de46185e38f52c79ff4ebb1f8ad592e155835317dd49a62b21063bee844210a19517320381862aa4c3')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
