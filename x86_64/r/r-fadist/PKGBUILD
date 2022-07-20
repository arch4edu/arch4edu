# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=FAdist
_pkgver=2.4
pkgname=r-${_pkgname,,}
pkgver=2.4
pkgrel=5
pkgdesc='Distributions that are Sometimes Used in Hydrology'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('38e5293e7011bf4cbced147eb5bd89adda1f10a0c7121ca5089dcee7504cdc98')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
