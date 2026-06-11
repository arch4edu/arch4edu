# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>

_pkgname=survey
_pkgver=4.5
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
  r-knitr
  r-quantreg
  r-r.rsp
  r-rsqlite
  r-summer
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('4d424593ffd252886cf6c9c81d4bcd26')
b2sums=('51cdfde1375507711be8ea74febe38bbb769be848f7c08806976f6d600b8fa316406728a13e8f54f2dfa43c8790ad1909db35c89b7c8281a04d9b24efcc4b08a')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
