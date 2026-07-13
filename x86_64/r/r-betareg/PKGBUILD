# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=betareg
_pkgver=3.2-5
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
md5sums=('5640969e432e635e67c6c1524dc877ee')
b2sums=('5aba68fd809e8e6363af87573c18ab89ed2de8888b434be538b800a285e8542367a15c76daa7bfae8947845a57bd6fab8eedffcc22a44100861f035836191095')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
