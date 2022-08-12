# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=statmod
_pkgver=1.4.37
pkgname=r-${_pkgname,,}
pkgver=1.4.37
pkgrel=1
pkgdesc='Statistical Modeling'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
optdepends=(
  r-mass
  r-tweedie
)
makedepends=(
  gcc-fortran
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('90d2c8a79e0cb291f2685686436bcf4c5b9abd2efb84759a8553d1b1adb76913')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
