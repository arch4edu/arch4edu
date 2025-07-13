# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>

_pkgname=CompQuadForm
_pkgver=1.4.4
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Distribution Function of Quadratic Forms in Normal Variables"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('44e119935fa15aa034de317d41e801d8')
b2sums=('a52e7d20c609f1243aad46779b8e98eaa86a5f5d26afed6bb4355997bf354c722eb7d682c3bab532eadb13a6a7a08cca1962153c0092e2b34533e2d5a9438116')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
