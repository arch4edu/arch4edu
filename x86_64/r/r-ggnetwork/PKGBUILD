# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=ggnetwork
_pkgver=0.5.14
pkgname=r-${_pkgname,,}
pkgver=0.5.14
pkgrel=1
pkgdesc="Geometries to Plot Networks with 'ggplot2'"
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-ggplot2
  r-ggrepel
  r-igraph
  r-network
  r-sna
)
optdepends=(
  r-knitr
  r-rmarkdown
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('caab79d85a817608e9a9d827783f157393fc3f2b9de8c20669699175a19f3ff0')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
