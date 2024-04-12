# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=rsm
_pkgver=2.10.4
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="Response-Surface Analysis"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-estimability
)
optdepends=(
  r-conf.design
  r-doe.base
  r-emmeans
  r-frf2
  r-vdgraph
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('2d35944cadf6049288e007592868015c')
b2sums=('a5f3b27311c29444cddba1ee9339a7011c8fb2f735280a18dde6d0c48af3df46355f3d794230ce5002878d6b75f6a94a9e03964a4cb258d5b7fc0efd1101ad56')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
