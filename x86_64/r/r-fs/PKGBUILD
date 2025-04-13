# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Alex Branham <alex.branham@gmail.com>

_pkgname=fs
_pkgver=1.6.6
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Cross-Platform File System Operations Based on 'libuv'"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  libuv
  r
)
optdepends=(
  r-covr
  r-crayon
  r-knitr
  r-pillar
  r-rmarkdown
  r-spelling
  r-testthat
  r-tibble
  r-vctrs
  r-withr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz"
        "system-libuv.patch")
md5sums=('61b8a3ee43759ed4718659cf7f499cc1'
         '312c9ec1662d8ebecd388a771ae1a903')
b2sums=('575d044f1bbd4a49a3c61b7b2bc136e945e08b3a8aaf18cf9d10f15f3ed8dbb2b9d998e75c1210443226e8b098a58650a3a0c093a845a6c78a174cf57a5af7e0'
        'ac55bda314e4a9c184b820a7194b421bcac65ff739cf14c5d9af9004ec717fc99db159e0c02ff7060f2ed2a8f0147bc8f0a29d0cb1d760af5c057feb08c9c33a')

prepare() {
  # build against system libuv
  patch -Np1 -i system-libuv.patch
}

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
