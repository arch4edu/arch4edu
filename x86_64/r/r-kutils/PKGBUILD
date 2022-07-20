# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=kutils
_pkgver=1.70
pkgname=r-${_pkgname,,}
pkgver=1.70
pkgrel=5
pkgdesc='Project Management Tools'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-openxlsx
  r-plyr
  r-runit
  r-xtable
)
optdepends=(
  r-rockchalk
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('67d0a03ad600ed7f4eea072476baa0664c3fb2d116c326856b550ebcb831531a')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
