# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=rngWELL
_pkgver=0.10-9
pkgname=r-${_pkgname,,}
pkgver=0.10.9
pkgrel=1
pkgdesc='Toolbox for WELL Random Number Generators'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('BSD')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('9969cc10be6d18155d2b2de93381c52e7f720c2b1b3f2554fa8bfa84ceb7cacb')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
  install -Dm644 "${_pkgname}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
