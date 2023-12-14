# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=tensorA
_pkgver=0.36.2.1
pkgname=r-${_pkgname,,}
pkgver=0.36.2.1
pkgrel=1
pkgdesc='Advanced Tensor Arithmetic with Named Indices'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('06588261fe7dff6a8edafe2b9d436b39a3b46c754f2ed327ae6322561a617db7')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
