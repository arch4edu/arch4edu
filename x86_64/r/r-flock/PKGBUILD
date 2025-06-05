# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=flock
_pkgver=0.7
pkgname=r-${_pkgname,,}
pkgver=0.7
pkgrel=4
pkgdesc='Process Synchronization Using File Locks'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('Apache')
depends=(
  r
  r-rcpp
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('47ebdeaeeb63ec93c800782bafa7f2846f73bb905adb6a3b5c44b248ce1de9fd')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
