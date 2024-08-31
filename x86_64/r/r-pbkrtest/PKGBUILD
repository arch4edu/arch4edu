# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Taekyung Kim <Taekyung.Kim.Maths@gmail.com>

_pkgname=pbkrtest
_pkgver=0.5.3
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
md5sums=('d4501121ded98c6ced803b89c7abe4d9')
b2sums=('1d88cd24b7e28cb06de11b7d74d36cd46aa3b474c19ce1e960e18eaa5bbe304fa5f89e2df95971faef797f60ff571878dfbf546f088cd032577cb84e0a8c50d5')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
