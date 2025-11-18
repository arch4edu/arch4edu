# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=future
_pkgver=1.68.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Unified Parallel and Distributed Processing in R for Everyone"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('LGPL-2.1-or-later')
depends=(
  r-digest
  r-globals
  r-listenv
  r-parallelly
)
optdepends=(
  r-markdown
  r-r.rsp
  r-rhpcblasctl
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('199084df281a833a7b86bf69ccd652f7')
b2sums=('bcec7a41c8b2409088f53bf7a3f38e2e18a9c9396b0a66b1d6ffffcb44d6f9b88b0274647f983c83dccdce7b429d1d8e8ee549d78b2f42e32f9d7cacbf4f4cfd')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
