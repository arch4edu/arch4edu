# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=plm
_pkgver=2.6-7
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Linear Models for Panel Data"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-bdsmatrix
  r-collapse
  r-formula
  r-lmtest
  r-maxlik
  r-rdpack
  r-sandwich
  r-zoo
)
optdepends=(
  r-aer
  r-car
  r-fixest
  r-knitr
  r-lfe
  r-pder
  r-rmarkdown
  r-statmod
  r-texreg
  r-urca
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('bd79c8d75f24247ad46b7fa4c189376c')
b2sums=('306f1788ff844a22be6ff869638f7fc5cac016b998660e4e3174feb926eed32774d94437e8f0499ef17200c7166de4a6c1f20588e621f288c4eb482d4c5a9329')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
