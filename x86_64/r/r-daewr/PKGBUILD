# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=daewr
_pkgver=1.2-9
pkgname=r-${_pkgname,,}
pkgver=1.2.9
pkgrel=1
pkgdesc='Design and Analysis of Experiments with R'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-stringi
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('fb86af72ae4d8f81ffa0bc498fb9d972117b0bd95dbeaad8a989925750a0917a')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
