# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=jmvcore
_pkgver=28.3
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Dependencies for the 'jamovi' Framework"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-base64enc
  r-jsonlite
  r-r6
  r-rlang
)
optdepends=(
  r-commonmark
  r-export
  r-fastmap
  r-ggplot2
  r-jmvreadwrite
  r-knitr
  r-ragg
  r-rcolorbrewer
  r-rprotobuf
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('10effc81725efea7348e73dcb18a4178')
b2sums=('42ddfdb90415126942575c18cc549dda99630a408e9ec29a4941861efb8692837f575345fa19fbaaa6be8595155b690f39f0410ab00b3c905aaeaa9fe72f051b')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
