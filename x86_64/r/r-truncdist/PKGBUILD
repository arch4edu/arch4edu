# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=truncdist
_pkgver=1.0-2
pkgname=r-${_pkgname,,}
pkgver=1.0.2
pkgrel=4
pkgdesc='Truncated Random Variables'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-evd
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('b848b68bdd983bd496fa7327632ffa8add8d2231229b8af5c8bc29d823e1300a')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
