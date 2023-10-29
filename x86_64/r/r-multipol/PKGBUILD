# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=multipol
_pkgver=1.0-9
pkgname=r-${_pkgname,,}
pkgver=1.0.9
pkgrel=3
pkgdesc='Multivariate Polynomials'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-abind
)
optdepends=(
  r-polynom
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('4ec305565c214872705f7d5ea4928c8761750663d664a77f1676d81a1ca0c632')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
