# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=profmem
_pkgver=0.7.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Simple Memory Profiling for R"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('LGPL-2.1-or-later')
depends=(
  r
)
optdepends=(
  r-markdown
  r-microbenchmark
  r-r.rsp
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('3048707ef4f365b91a84e3974f3669a5')
b2sums=('f45e5e5078490559f0714ceb851ca72bcb6d8672d0a34604165c772df339309dde59cd4de64d4b0b15962e47f7b23b4125bccfe02099a9b607950de5b96fe6eb')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
