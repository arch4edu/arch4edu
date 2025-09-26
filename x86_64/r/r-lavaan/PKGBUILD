# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=lavaan
_pkgver=0.6-20
pkgname=r-${_pkgname,,}
pkgver=0.6.20
pkgrel=1
pkgdesc='Latent Variable Analysis'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-mnormt
  r-numderiv
  r-pbivnorm
  r-quadprog
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('c3df7b2ceb5b0c23c685beaad112e8160c0466c48518b8a83974ca025dc1c1c6')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
