# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=daewr
_pkgver=1.2-7
pkgname=r-${_pkgname,,}
pkgver=1.2.7
pkgrel=1
pkgdesc='Design and Analysis of Experiments with R'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-frf2
  r-stringi
)
optdepends=(
  r-r.rsp
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('87ea6cc327f2acd5479bf1ae749f4203ebddac5679d3c8b2588dfd5173ad108d')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
