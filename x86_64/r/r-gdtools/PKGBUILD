# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: portaloffreedom

_pkgname=gdtools
_pkgver=0.5.2
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Font Metrics and Font Management Utilities for R Graphics"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-only')
depends=(
  cairo
  freetype2
  r-fontquiver
  r-htmltools
  r-rcpp
  r-systemfonts
)
checkdepends=(
  r-gfonts
  r-testthat
)
optdepends=(
  r-curl
  r-gfonts
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('e907a613c135c7ab52adfbe1173972d5')
b2sums=('1e021867e5ea9baf287cc8fd6d0134318e25bbfbfac01ad4e751b69a35fd338d01804fbc043f653596ded09b1335a411e1ee28c7c320e68423ec749c00492e37')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

# check() {
#   cd "$_pkgname/tests"
#   R_LIBS="$srcdir/build" NOT_CRAN=true Rscript --vanilla testthat.R
# }

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
