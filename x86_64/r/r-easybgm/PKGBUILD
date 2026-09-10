# Maintainer: Jingbei Li <i@jingbei.li>
_cranname=easybgm
_pkgver=0.5.0
pkgname=r-easybgm
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Extracting and Visualizing Bayesian Graphical Models"
arch=(x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(GPLv3)
depends=(r r-bdgraph r-bggm r-bgms r-coda r-dplyr r-ggplot2 r-hdinterval r-igraph r-qgraph)
makedepends=(gcc-fortran)
optdepends=(r-testthat r-vdiffr)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_pkgver}.tar.gz")
sha256sums=('f8a555c844e9c4f79d80991ab0a173c31ea9972e61dfae0581d6e479536a1adb')

build() {
  R CMD INSTALL ${_cranname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
}
