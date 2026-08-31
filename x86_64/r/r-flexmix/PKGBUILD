# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=flexmix
_pkgver=2.3-21
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
md5sums=('ce906a36ba96df80ec3fd5548208bbd5')
b2sums=('6540e4aaa8692f6c8c3aea8d81fdb384be858691b951cd3399912e3edaeb8fba45f9d956be8980928c3b1bd92c2b122089a4449c616625c449f403bab96e1789')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
