# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=rsm
_pkgver=2.10.3
pkgname=r-${_pkgname,,}
pkgver=2.10.3
pkgrel=4
pkgdesc='Response-Surface Analysis'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-estimability
)
optdepends=(
  r-conf.design
  r-doe.base
  r-emmeans
  r-frf2
  r-vdgraph
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('ef72888ab05c8d9ac8750e83633de551973fe693fb0cd8e36d381fc587d592b5')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
