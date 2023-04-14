# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=partykit
_pkgver=1.2-20
pkgname=r-${_pkgname,,}
pkgver=1.2.20
pkgrel=1
pkgdesc='A Toolkit for Recursive Partytioning'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-formula
  r-inum
  r-libcoin
  r-mvtnorm
)
optdepends=(
  r-aer
  r-coin
  r-datasets
  r-mlbench
  r-parallel
  r-party
  r-pmml
  r-psychotools
  r-psychotree
  r-randomforest
  r-rjava
  r-rweka
  r-sandwich
  r-strucchange
  r-th.data
  r-vcd
  r-xml
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('63509aa3ed2d7417ad284c037cef66bc837fdb7a97967957e79b9fee8ed2e0da')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
