# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>

_pkgname=survey
_pkgver=4.4-2
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
md5sums=('565ca8d5fc141cbc6bcacdd8bc2e2f0f')
b2sums=('88901e62b49e9a6f57c5e9761d9d5b6e44b21465c3e6fe21c53ccb1e50775861cbcac2c2d2d0f5c35635b4ee2ccb57d786eb95e392480e81f8bf1c05a392699c')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
