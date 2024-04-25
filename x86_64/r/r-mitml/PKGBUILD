# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=mitml
_pkgver=0.4-5
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=4
pkgdesc="Tools for Multiple Imputation in Multilevel Modeling"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-haven
  r-jomo
  r-pan
)
optdepends=(
  r-amelia
  r-geepack
  r-glmmtmb
  r-knitr
  r-lavaan
  r-lme4
  r-mice
  r-miceadds
  r-rmarkdown
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('b241fc0514024cf248ab9dbd2914f880')
b2sums=('e35f0eadec62ba0f6df4e7215c07a1141bf15f87ba8c71f821236b7590d496a38bce234dd308ff357f4e98117734f6834c0cd6450421fccf4742711e91907f02')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
