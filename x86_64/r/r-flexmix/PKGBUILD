# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=flexmix
_pkgver=2.3-20
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Flexible Mixture Modeling"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-modeltools
)
optdepends=(
  r-actuar
  r-diptest
  r-ecdat
  r-ellipse
  r-gclus
  r-glmnet
  r-lme4
  r-mlbench
  r-multcomp
  r-mvtnorm
  r-suppdists
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('981391fa78fc62d6fa2c1891c32fc6ce')
b2sums=('d35f9f9a384568fc8ed4f9223cd7a6f88f2a86a7fea36e410ebde9ea61d27bfaacbb1be066441baf2e11e10fb2c10a012d9ba5a2047a2ed5d486a1e584ab4fa6')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
