# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=fastICA
_pkgver=1.2-3
pkgname=r-${_pkgname,,}
pkgver=1.2.3
pkgrel=4
pkgdesc='FastICA Algorithms to Perform ICA and Projection Pursuit'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
optdepends=(
  r-mass
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('e9ef82644cb64bb49ae3b7b6e0885f4fb2dc08ae030f8c76fe8dd8507b658950')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
