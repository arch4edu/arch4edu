# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=stringfish
_pkgver=0.19.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Alt String Implementation"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-only')
depends=(
  onetbb
  pcre2
  r-rcpp
  r-rcppparallel
  xxhash
)
optdepends=(
  r-knitr
  r-rmarkdown
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz"
        "system-libs.patch")
md5sums=('086fd63ec72d189b62711df59d92c29c'
         '685b52efc1bfcd2574e559f9df64560e')
b2sums=('af1f1f0f649471150794e0c46b28c4acda97a2167d6a9aaa462a4dcaae1ebfafcca26db880ca0b6ceddace7caecfe968af9a876e22735f4ced39d806525e8703'
        'a56459ada70af48192f87952f0bf3c7badf8f9f0159a9ef1cef6d0c9bb9d1faaaa61d82c4a91b4538cd37b3cbca657ddd744ce910379500a8ed8fca7f7a4fd35')

# prepare() {
#   # use system xxhash
#   patch -Np1 -i system-libs.patch
# }

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
