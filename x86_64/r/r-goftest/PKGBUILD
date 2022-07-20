# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=goftest
_pkgver=1.2-3
pkgname=r-${_pkgname,,}
pkgver=1.2.3
pkgrel=4
pkgdesc='Classical Goodness-of-Fit Tests for Univariate Distributions'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('3a5f74b6ae7ece5b294781ae57782abe12375d61789c55ff5e92e4aacf347f19')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
