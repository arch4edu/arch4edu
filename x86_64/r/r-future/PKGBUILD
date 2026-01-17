# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=future
_pkgver=1.69.0
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
md5sums=('78ed1f0a66874404b1f1ba33ea2ffada')
b2sums=('f2d45a34eb304f79b60f0ed4bbd40e053e6a7fa5cb5b31b6b89eac815a9fef50547d0872f0cd1127efb64653140f3fd64f282a8456538c09b2182c356b9b6c47')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
