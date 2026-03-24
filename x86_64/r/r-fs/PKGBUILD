# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Alex Branham <alex.branham@gmail.com>

_pkgname=fs
_pkgver=2.0.1
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
        )
md5sums=('d6acfc5d51002f04a7f159131034b438')
b2sums=('2db467d36c44f84b5650e2888afe575b01d03f91778919aea121e863e27b1ee350154eb5e40b71b2edfeadce3daee2a4efd83ac7b775095a2d5c903d209af593')

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
