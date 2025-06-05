# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=HSAUR3
_pkgver=1.0-15
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="A Handbook of Statistical Analyses Using R (3rd Edition)"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  r
)
optdepends=(
  r-ape
  r-coin
  r-flexmix
  r-formula
  r-gamair
  r-gamlss.data
  r-gee
  r-hsaur2
  r-lme4
  r-maps
  r-mboost
  r-mclust
  r-mice
  r-mlbench
  r-multcomp
  r-mvtnorm
  r-partykit
  r-quantreg
  r-randomforest
  r-rmeta
  r-sandwich
  r-scatterplot3d
  r-sf
  r-sp
  r-th.data
  r-vcd
  r-wordcloud
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('ad511d4510711a4c8519f386d72e3c05')
b2sums=('442fa3d9a349a2dabea4a8553cd9ae43fbce48c1453c246d86a4a2f8739d73b1301ff615a101652e89c0164dc7d998ab56aa5204b76422e68934901ba5d65b44')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
