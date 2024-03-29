# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=loo
_pkgver=2.7.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Efficient Leave-One-Out Cross-Validation and WAIC for Bayesian Models"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-or-later')
depends=(
  pandoc
  r-checkmate
  r-matrixstats
  r-posterior
)
optdepends=(
  r-bayesplot
  r-brms
  r-ggplot2
  r-knitr
  r-rmarkdown
  r-rstan
  r-rstanarm
  r-rstantools
  r-spdep
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('f603c34f25a3c083c2a2b4760afa932f')
b2sums=('90ed3e766eacb2d6cc4838e7b8b05876fab4f69dabd3f0c424c29b666c55ad091a68eb526870df74e62217949327ca82cac3f97fd9698361a04e0d30f9a6340e')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
