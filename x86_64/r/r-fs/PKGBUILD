# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Alex Branham <alex.branham@gmail.com>

_pkgname=fs
_pkgver=1.6.5
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
md5sums=('92e1204fc8d567e5fedc06e0ac9e8c1d'
         'e9cd06be1a987fd1cdab9b577736bfe0')
b2sums=('da106a009c7768572702bdc92ffd8ddd6ed7d877ab99cda4e3f0358de3f427a6b29195a329b2a8586f0c2f901b708582499ad833ac6e66d19239a11b70030d28'
        'bb5f52cc3b73def81bc7688817dcfcf79b69d9cf2522521d389a78e55002ea22409b9f159a9d7e2a682d59148f3138245bc9e92971ceaa0246727f3fbb7b1bc1')

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
