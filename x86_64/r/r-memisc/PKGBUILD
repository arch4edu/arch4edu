# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=memisc
_pkgver=0.99.31.8.3
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Management of Survey Data and Presentation of Analysis Results"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only OR GPL-3.0-only')
depends=(
  r-data.table
  r-jsonlite
  r-yaml
)
optdepends=(
  r-knitr
  r-rmarkdown
  r-sandwich
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('6c9cebea0191b9be33f730fcac274602')
b2sums=('555b47f667083163055bfa1ce8fa78ac8f0be71de5a8f77491676c5cc053500b28bb6967f91c53f4c3f5392b9daf9f30c37fda79b1a94f8b210735f8b6ecd7b3')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
