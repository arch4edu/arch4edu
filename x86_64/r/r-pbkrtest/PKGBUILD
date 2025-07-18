# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Taekyung Kim <Taekyung.Kim.Maths@gmail.com>

_pkgname=pbkrtest
_pkgver=0.5.5
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Parametric Bootstrap, Kenward-Roger and Satterthwaite Based Methods for Test in Mixed Models"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-broom
  r-doby
  r-dplyr
  r-lme4
  r-numderiv
)
optdepends=(
  r-knitr
  r-markdown
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('8df1c5b2fdd2ddd3237f1a4c07bbb365')
b2sums=('cfb2d168e32f7aed3b2967b19282882b0550b29a6d547daaaeb37e09a65f5cfc9159d71c280028ce2290838f94469b54740fdda4d7cada0963e2efddb8d7f5ed')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
