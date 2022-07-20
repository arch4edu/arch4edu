# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=mdscore
_pkgver=0.1-3
pkgname=r-${_pkgname,,}
pkgver=0.1.3
pkgrel=7
pkgdesc='Improved Score Tests for Generalized Linear Models'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
optdepends=(
  r-sleuth3
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('12f5841258f7d9bdc8074244bfb76482df0e480f09835d666c90a5364d2e9481')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
