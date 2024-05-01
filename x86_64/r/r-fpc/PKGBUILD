# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=fpc
_pkgver=2.2-12
pkgname=r-${_pkgname,,}
pkgver=2.2.12
pkgrel=1
pkgdesc='Flexible Procedures for Clustering'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-diptest
  r-flexmix
  r-kernlab
  r-mclust
  r-prabclus
  r-robustbase
)
optdepends=(
  r-mvtnorm
  r-pdfcluster
  r-tclust
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('555996b4c7e78a28067df25ac657b5065ec79b6b2cd76080382c2d5b43104787')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
