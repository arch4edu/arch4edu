# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=desirability
_pkgver=2.1
pkgname=r-${_pkgname,,}
pkgver=2.1
pkgrel=5
pkgdesc='Function Optimization and Ranking via Desirability Functions'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
optdepends=(
  r-lattice
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('b33af2ce184532b819f21a959af0b752991b764ef301051873141865eeee8f24')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
