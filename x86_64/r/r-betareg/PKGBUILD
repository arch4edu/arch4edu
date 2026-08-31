# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=betareg
_pkgver=3.2-6
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
md5sums=('7ade6a3995ba1c2374a0c11e75828315')
b2sums=('bce49206431b5c4cbcc115aab8399c650925bf7baeebe9cdb463fb49dd4f6a756e1f85aa6a8e6aa151fda5655ef960bf9f2085154075487362234a41e7ced461')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
