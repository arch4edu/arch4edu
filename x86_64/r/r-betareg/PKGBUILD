# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=betareg
_pkgver=3.2-4
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Beta Regression"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only OR GPL-3.0-only')
depends=(
  r-flexmix
  r-formula
  r-lmtest
  r-modeltools
  r-sandwich
)
optdepends=(
  r-car
  r-distributions3
  r-knitr
  r-numderiv
  r-partykit
  r-quarto
  r-statmod
  r-strucchange
  r-bamlss
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('d43ac56609dd9fe67f75591fea2369e1')
b2sums=('58a454aa1bd32aded9bf5880de3630587e8a5404a8b0d1435a9ab6ce1eabe4ad47d9df8828879f3f927271566114a47fa114fcd7f2ca501d2a87128022e71bdd')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
