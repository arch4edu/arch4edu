# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=fastICA
_pkgver=1.2-4
pkgname=r-${_pkgname,,}
pkgver=1.2.4
pkgrel=1
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
sha256sums=('ed6988ea410d1a75bf4f4925edcac5a660a417e33ba0a939bc0351e534df5f2f')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
