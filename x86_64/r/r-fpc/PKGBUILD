# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=fpc
_pkgver=2.2-10
pkgname=r-${_pkgname,,}
pkgver=2.2.10
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
sha256sums=('99b4548f2eca1a092a31bc2fa4e4bd1d6b50fdfacf3218588c879ceec99147d2')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
