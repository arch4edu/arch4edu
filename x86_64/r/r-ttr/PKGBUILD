# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=TTR
_pkgver=0.24.4
pkgname=r-${_pkgname,,}
pkgver=0.24.4
pkgrel=1
pkgdesc='Technical Trading Rules'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-curl
  r-xts
  r-zoo
)
optdepends=(
  r-quantmod
  r-runit
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('89732b9c359bae2f41cd23db649f0897c10fab0702d780c4c25a997322710284')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
