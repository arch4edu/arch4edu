# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=rsm
_pkgver=2.10.4
pkgname=r-${_pkgname,,}
pkgver=2.10.4
pkgrel=1
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
sha256sums=('505445b2f06b4e306fdacfaecc0c26327b96e2828ffab4e1ccfa8320c19d02ae')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
