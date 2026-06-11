# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=party
_pkgver=1.3-20
pkgname=r-${_pkgname,,}
pkgver=1.3.20
pkgrel=1
pkgdesc='A Laboratory for Recursive Partytioning'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-coin
  r-modeltools
  r-mvtnorm
  r-sandwich
  r-strucchange
  r-zoo
)
optdepends=(
  r-colorspace
  r-ipred
  r-mass
  r-mlbench
  r-randomforest
  r-th.data
  r-varimp
  r-vcd
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('e933135db2fff13e5ae22a5272f9a624731a2e10d0efc05e9ecab18e5ea48457')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
