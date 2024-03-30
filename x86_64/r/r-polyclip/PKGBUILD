# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=polyclip
_pkgver=1.10-6
pkgname=r-${_pkgname,,}
pkgver=1.10.6
pkgrel=1
pkgdesc='Polygon Clipping'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('BSL')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('3c2f13edabdd9cd2612a60afec9ba447b3dd5a4109dd066d7870411d032f8b63')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
