# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=AER
_pkgver=1.2-17
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Applied Econometrics with R"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only OR GPL-3.0-only')
depends=(
  r-car
  r-formula
  r-lmtest
  r-sandwich
  r-zoo
)
optdepends=(
  r-dynlm
  r-effects
  r-fgarch
  r-forecast
  r-ineq
  r-longmemo
  r-mlogit
  r-np
  r-plm
  r-pscl
  r-quantreg
  r-rgl
  r-rocr
  r-rugarch
  r-sampleselection
  r-scatterplot3d
  r-strucchange
  r-systemfit
  r-truncreg
  r-tseries
  r-urca
  r-vars
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('d30ad6dfbb52a9e19654403eb487d6cc')
b2sums=('606475ff4b1c84a6cb97ad4256d250b01542a796cc11e8b66f18e2b4b91862434df493b1b203f465513838f1ffd874642f8cfe48c7104d32a767aa594ca4f036')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
