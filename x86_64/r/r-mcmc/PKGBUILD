# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=mcmc
_pkgver=0.9-7
pkgname=r-${_pkgname,,}
pkgver=0.9.7
pkgrel=4
pkgdesc='Markov Chain Monte Carlo'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('MIT')
depends=(
  r
)
optdepends=(
  r-iso
  r-xtable
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('b7c4d3d5f9364c67a4a3cd49296a61c315ad9bd49324a22deccbacb314aa8260')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
  install -Dm644 "${_pkgname}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
