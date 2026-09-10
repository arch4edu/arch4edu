# Maintainer: Jingbei Li <i@jingbei.li>
_cranname=bgms
_pkgver=0.2.0.0
pkgname=r-bgms
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Bayesian Analysis of Networks of Binary and/or Ordinal Variables"
arch=(x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(GPLv3)
depends=(r r-dqrng r-lifecycle r-rcpp r-rcppparallel r-rdpack r-s7)
makedepends=(gcc-fortran r-bh r-rcpparmadillo)
optdepends=(r-coda r-covr r-ggplot2 r-knitr r-qgraph r-rmarkdown r-testthat r-withr)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_pkgver}.tar.gz")

build() {
  R CMD INSTALL ${_cranname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
}
sha256sums=('43d137985febf5956bab707ea4cab53bccb5cd13007496d16454a4af2da257d2')
