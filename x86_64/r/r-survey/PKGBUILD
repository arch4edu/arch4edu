# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>

_pkgname=survey
_pkgver=4.4-8
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Analysis of Complex Survey Samples"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only OR GPL-3.0-only')
depends=(
  r-minqa
  r-mitools
  r-numderiv
  r-rcpp
)
makedepends=(
  r-rcpparmadillo
)
optdepends=(
  r-aer
  r-compquadform
  r-dbi
  r-hexbin
  r-quantreg
  r-r.rsp
  r-rsqlite
  r-summer
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('0073d155ca38e08e4347f74f8b66b2af')
b2sums=('9a2db93c4d882b84aa99f97dc45a586114bf05147b88e620611eb8ce90e457179bc54c7058afddbc57c65368848c9318117870ceb1ac0649954e3d93d67235f1')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
