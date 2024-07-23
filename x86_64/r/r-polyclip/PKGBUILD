# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=polyclip
_pkgver=1.10-7
pkgname=r-${_pkgname,,}
pkgver=1.10.7
pkgrel=1
pkgdesc='Polygon Clipping'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('BSL')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('f58eaac3a5b2f6711c0c5f12fff91cf80a245ae45878f7217880ab062b5550d3')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
