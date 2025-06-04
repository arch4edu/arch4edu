# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Taekyung Kim <Taekyung.Kim.Maths@gmail.com>

_pkgname=pbkrtest
_pkgver=0.5.4
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
md5sums=('db9c2cb28d888f5d6bf4c969dee705a6')
b2sums=('145c5dd9d9673a3aaec13842ebbcb6cbc9539ee215843f63cd63123c711f176f1c6d8090a5ea86635a9e33448e31261f50458f6b0fddbb811e0d893f65076ac5')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
