# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=coin
_pkgver=1.4-2
pkgname=r-${_pkgname,,}
pkgver=1.4.2
pkgrel=7
pkgdesc='Conditional Inference Procedures in a Permutation Test Framework'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-libcoin
  r-matrixstats
  r-modeltools
  r-multcomp
  r-mvtnorm
)
optdepends=(
  r-e1071
  r-th.data
  r-vcd
  r-xtable
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('7546d1f27a82d98b4b3e43e4659eba0f74a67d5919ce85d2fb360282ba3cfbb2')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
