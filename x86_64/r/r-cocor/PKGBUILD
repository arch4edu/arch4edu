# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=cocor
_pkgver=1.1-4
pkgname=r-${_pkgname,,}
pkgver=1.1.4
pkgrel=1
pkgdesc='Comparing Correlations'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
optdepends=(
  r-rkward
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('28f8bf5ffd647675ed9b28d2e3a28cc97cb9dc996095caccd0aac6dfa9451416')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
