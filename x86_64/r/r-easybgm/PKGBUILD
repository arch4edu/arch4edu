# Maintainer: Jingbei Li <i@jingbei.li>
_cranname=easybgm
_pkgver=0.4.0
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
sha256sums=('39e194057dd9ddf6a897148212e5c8bf28d77b5fbaff0bea1a4fc8422b1c2c06')

build() {
  R CMD INSTALL ${_cranname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
}
