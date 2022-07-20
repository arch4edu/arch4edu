# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=sgt
_pkgver=2.0
pkgname=r-${_pkgname,,}
pkgver=2.0
pkgrel=5
pkgdesc='Skewed Generalized T Distribution Tree'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-numderiv
  r-optimx
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('7dd2ba6632dea71b8a76df6d879e2fd036353fcfae5d0788768ab758a4aa6361')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
