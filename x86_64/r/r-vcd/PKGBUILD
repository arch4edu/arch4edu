# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=vcd
_pkgver=1.4-13
pkgname=r-${_pkgname,,}
pkgver=1.4.13
pkgrel=1
pkgdesc='Visualizing Categorical Data'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-colorspace
  r-lmtest
)
optdepends=(
  r-coin
  r-hsaur3
  r-kernlab
  r-kernsmooth
  r-mvtnorm
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('9dac62ace393ef6e56a1f5fa8909081350d2f9f46e47ea6f78759d41a81df8cc')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
