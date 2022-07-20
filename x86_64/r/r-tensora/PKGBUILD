# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=tensorA
_pkgver=0.36.2
pkgname=r-${_pkgname,,}
pkgver=0.36.2
pkgrel=4
pkgdesc='Advanced Tensor Arithmetic with Named Indices'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('8e8947566bd3b65a54de4269df1abaa3d49cf5bfd2a963c3274a524c8a819ca7')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
