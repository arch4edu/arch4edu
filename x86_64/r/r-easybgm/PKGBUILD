# Maintainer: Jingbei Li <i@jingbei.li>
_cranname=easybgm
_pkgver=0.5.1
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
sha256sums=('270f4b707525f12893d5383be6b2649f75ab4fb5dfaff14391ae9d812de2c723')

build() {
  R CMD INSTALL ${_cranname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
}
