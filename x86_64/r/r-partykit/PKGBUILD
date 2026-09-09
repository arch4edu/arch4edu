# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=partykit
_pkgver=1.3-0
pkgname=r-${_pkgname,,}
pkgver=1.3.0
pkgrel=2
pkgdesc='A Toolkit for Recursive Partytioning'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL-2.0-only OR GPL-3.0-only')
depends=(
  r-formula
  r-inum
  r-libcoin
  r-mvtnorm
  r-strucchange
)
optdepends=(
  r-aer
  r-bibtex
  r-coin
  r-knitr
  r-mlbench
  r-party
  r-psychotools
  r-psychotree
  r-randomforest
  r-rjava
  r-rweka
  r-sandwich
  r-th.data
  r-vcd
  r-xml
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('1427b960dff3d988db499f1dbe8b43f395dfbc4057e3d827330ed4d27b6a403a')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
