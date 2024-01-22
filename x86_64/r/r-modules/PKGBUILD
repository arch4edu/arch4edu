# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=modules
_pkgver=0.13.0
pkgname=r-${_pkgname,,}
pkgver=0.13.0
pkgrel=1
pkgdesc='Self Contained Units of Source Code'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('MIT')
depends=(
  r
)
optdepends=(
  r-devtools
  r-knitr
  r-lintr
  r-parallel
  r-rmarkdown
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('553b42f26627db265de5279f93f4b1f9d141d67e51c8f56b86e86fd6a5b7c7fc')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
  install -Dm644 "${_pkgname}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
