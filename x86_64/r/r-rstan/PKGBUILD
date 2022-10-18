# system requirements: GNU make, pandoc
# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Ward Segers <w@rdsegers.be>
# Contributor: Alex Branham <alex.branham@gmail.com>

_pkgname=rstan
_pkgver=2.21.7
pkgname=r-${_pkgname,,}
pkgver=2.21.7
pkgrel=3
pkgdesc='R Interface to Stan'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-bh
  r-ggplot2
  r-gridextra
  r-inline
  r-loo
  r-pkgbuild
  r-rcpp
  r-rcppeigen
  r-rcppparallel
  r-stanheaders
  make
  pandoc
)
optdepends=(
  r-bayesplot
  r-bh
  r-kernsmooth
  r-knitr
  r-matrix
  r-parallel
  r-rcppeigen
  r-rmarkdown
  r-rstantools
  r-rstudioapi
  r-runit
  r-shinystan
  r-v8
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('4495221310d390925b665c32e05ffabd3ae8857225bda65131a7ed2be41d6d45')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
