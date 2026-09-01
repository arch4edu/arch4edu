# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>

_pkgname=mitools
_pkgver=2.7
pkgname=r-${_pkgname,,}
pkgver=2.7
pkgrel=1
pkgdesc='Tools for Multiple Imputation of Missing Data'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-dbi
)
optdepends=(
  r-foreign
  r-rodbc
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('805584eae67e1e9c5af8a707d5d7c8f75a4453cbc0206cf9eaad0b3cf8596deb')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
