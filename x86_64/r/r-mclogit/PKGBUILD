# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=mclogit
_pkgver=0.9.15
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Multinomial Logit Models for Categorical Responses and Discrete Choices"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  r-memisc
)
optdepends=(
  r-knitr
  r-rmarkdown
  r-ucminf
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('792d66e15546a2ea3cb0a856c84fceec')
b2sums=('90ee27e91c55ebfd4ebd661dd7142660893e74c1cd7396e56af1444975ea77036c8de9108fe859e2a7899ff6f69fe035025fddbdce53eab99fbba4afbf51683f')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
