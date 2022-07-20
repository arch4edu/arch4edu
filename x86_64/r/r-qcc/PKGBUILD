# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=qcc
_pkgver=2.7
pkgname=r-${_pkgname,,}
pkgver=2.7
pkgrel=7
pkgdesc='Quality Control Charts'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
optdepends=(
  r-knitr
  r-rmarkdown
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('ff139a046e6b139ac25537b69be24e0ff32d6a39db6c941d1d02b4710f378251')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
