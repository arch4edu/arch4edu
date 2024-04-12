# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=bbmle
_pkgver=1.0.25.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="Tools for General Maximum Likelihood Estimation"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-bdsmatrix
  r-mvtnorm
  r-numderiv
)
optdepends=(
  r-aiccmodavg
  r-emdbook
  r-ggplot2
  r-hmisc
  r-knitr
  r-mumin
  r-optimx
  r-rms
  r-runit
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('73de3800a92640884c5db0e85724cdd3')
b2sums=('0c881ad4cb9ae16c660365b5abd2cd0e42893c614e0618b9505ad08d21df536d1f4cb5aa4d085e7fc77862a3e012a87458155e1abd13cf2731a857a3b4774af6')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
