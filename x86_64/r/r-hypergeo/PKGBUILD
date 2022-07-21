# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=hypergeo
_pkgver=1.2-13
pkgname=r-${_pkgname,,}
pkgver=1.2.13
pkgrel=4
pkgdesc='The Gauss Hypergeometric Function'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-contfrac
  r-desolve
  r-elliptic
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('6d5b78353aad1d13091ccbeb340867dad7b9eb00d0e2185286dc7e13848f4d8e')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
