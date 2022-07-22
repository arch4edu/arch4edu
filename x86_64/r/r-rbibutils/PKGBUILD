# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=rbibutils
_pkgver=2.2.8
pkgname=r-${_pkgname,,}
pkgver=2.2.8
pkgrel=3
pkgdesc="Read 'Bibtex' Files and Convert Between Bibliography Formats"
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
optdepends=(
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('f1aecdeeba99042d34de19234238c5bbdc18a26f271f6adf9c9b7e349d50d152')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
