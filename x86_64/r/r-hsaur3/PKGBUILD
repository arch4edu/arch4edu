# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=HSAUR3
_pkgver=1.0-16
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
md5sums=('2e375437565bc13c0c96df3f5a016783')
b2sums=('5769eceee2cbb8d87a6b71b4918defba236d7bafb3fd1dfc153dd7c4ff708e4a28d75fc117822aed7669fa4a86d9982a86fa8f26120e986a5127d05e80d2b1f3')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
