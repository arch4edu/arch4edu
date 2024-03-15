# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=poorman
_pkgver=0.2.7
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="A Poor Man's Dependency Free Recreation of 'dplyr'"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r
)
optdepends=(
  r-knitr
  r-rmarkdown
  r-roxygen2
  r-tinytest
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('4bbc26912e651669c58e9eab98856f0f')
b2sums=('9193ee73722ee4e26ded6d258429f665e51d17cc3ce233822a708febd856a47669dc904b0c1323d15fc58c95067b409a1aefb5e8462116d826de20f0932da6ef')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"

  install -d "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "/usr/lib/R/library/$_pkgname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"
}
