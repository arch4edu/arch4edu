# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=flexmix
_pkgver=2.3-19
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=3
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
md5sums=('f527d75cdb77e567d6e3b29c386f7a34')
b2sums=('3f1bb6fb6805ef4d883122220f1d9734c572136685bde692c4bfa7feaffc6457e34e588f5871d91ac0734d6c9c4df5adf3a68aa30879cb617db96d360a27c4ea')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
