# system requirements: pari/gp
# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=elliptic
_pkgver=1.4-0
pkgname=r-${_pkgname,,}
pkgver=1.4.0
pkgrel=5
pkgdesc='Weierstrass and Jacobi Elliptic Functions'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  pari
)
optdepends=(
  r-calibrator
  r-emulator
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('b65729b1a1c7a84a5b1a59bfc893a2d35106853eaadcae31cda5c9ee3c500bb6')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
