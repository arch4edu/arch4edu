# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=HDInterval
_pkgver=0.2.2
pkgname=r-${_pkgname,,}
pkgver=0.2.2
pkgrel=4
pkgdesc='Highest (Posterior) Density Intervals'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
optdepends=(
  r-coda
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('047eeb08c3dba21dc1cba8e35e3191cde6cdc98c77ee3a3496e045f7937565ed')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
