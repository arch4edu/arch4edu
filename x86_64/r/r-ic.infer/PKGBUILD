# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=ic.infer
_pkgver=1.1-6
pkgname=r-${_pkgname,,}
pkgver=1.1.6
pkgrel=6
pkgdesc='Inequality Constrained Inference in Linear Normal Situations'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-quadprog
  r-mvtnorm
  r-kappalab
)
optdepends=(
  r-relaimpo
)

source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('fea55a85cef922b2fc96a2e770cf8feea2c9a71208d7e4e7277989544ae76c93')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
