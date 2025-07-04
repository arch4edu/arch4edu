# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=fitdistrplus
_pkgver=1.2-4
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Help to Fit of a Parametric Distribution to Non-Censored or Censored Data"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-rlang
)
optdepends=(
  r-actuar
  r-bookdown
  r-gamlss.dist
  r-generalizedhyperbolic
  r-ggplot2
  r-hmisc
  r-knitr
  r-mc2d
  r-rgenoud
  r-rmarkdown
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('06e36b6c728d162503e276ca5659c536')
b2sums=('5d33f8432fcc23793e56e96f42692466d0daf57716bac3e19596a43290d7097e0929ebc1808dcb44e2b79444644a30025666a6e574f0e689962979cb02673161')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
