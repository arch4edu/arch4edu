# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=plm
_pkgver=2.6-6
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
md5sums=('37fd2cfc5fff13158c70dd0fca0f5c3b')
b2sums=('05f3be55605a014404c1ecce4259836ff59ee9eabba761da6a4795d336ac5e862c60f6801ba0a440e8841dc9e5e3b1d7fd8384780de370247e8f1f6809441045')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
