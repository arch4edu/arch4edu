# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=multipol
_pkgver=1.0-7
pkgname=r-${_pkgname,,}
pkgver=1.0.7
pkgrel=1
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
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('0abe3c894c0d8e928a920e73708a397133386a0d73a1e7952c4075afe67879e6')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
