# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contribitor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contribitor: frichtlm <frichtlm@gmail.com>
# Contribitor: wagnerflo <florian@wagner-flo.net>

_pkgname=reshape2
_pkgver=1.4.5
pkgname=r-${_pkgname,,}
pkgver=1.4.5
pkgrel=1
pkgdesc='Flexibly Reshape Data: A Reboot of the Reshape Package'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('MIT')
depends=(
  r
  r-plyr
  r-rcpp
  r-stringr
)
optdepends=(
  r-covr
  r-lattice
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('0ead5acd0153e5073b3c24e8e782982a4eab3aaa768ba17700d796fb13b68cef')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
  install -Dm644 "${_pkgname}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
