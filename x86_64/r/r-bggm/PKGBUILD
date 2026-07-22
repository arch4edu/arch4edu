# Maintainer: Jingbei Li <i@jingbei.li>
_cranname=BGGM
_pkgver=2.1.6
pkgname=r-bggm
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Bayesian Gaussian Graphical Models"
arch=(x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(GPL-2)
depends=(r r-bfpack r-ggally r-ggplot2 r-ggridges r-mvnfast r-network r-rcpp r-rdpack r-reshape r-sna)
makedepends=(gcc-fortran r-rcpparmadillo r-rcppdist r-rcppprogress)
optdepends=(r-abind r-assortnet r-knitr r-mice r-networktools r-psych r-rmarkdown r-testthat)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_pkgver}.tar.gz")
sha256sums=('83575cc71d23d0f310378a75c3e6f4307c34facbfb463921260c66f69796753f')

build() {
  R CMD INSTALL ${_cranname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
}
