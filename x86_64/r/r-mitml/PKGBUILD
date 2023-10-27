# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=mitml
_pkgver=0.4-5
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=3
pkgdesc="Tools for Multiple Imputation in Multilevel Modeling"
arch=(any)
url="https://cran.r-project.org/package=${_pkgname}"
license=(GPL)
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
sha256sums=('056aec823187cc3793640d8a5e74d74093bae74260a975ceb098a83a52e2eeeb')

build() {
  mkdir -p build
  R CMD INSTALL "$_pkgname" -l build
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
