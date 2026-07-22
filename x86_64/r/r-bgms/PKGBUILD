# Maintainer: Jingbei Li <i@jingbei.li>
_cranname=bgms
_pkgver=0.1.6.3
pkgname=r-bgms
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Bayesian Analysis of Networks of Binary and/or Ordinal Variables"
arch=(x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(GPLv3)
depends=(r r-coda r-dqrng r-lifecycle r-rcpp r-rcppparallel r-rdpack)
makedepends=(gcc-fortran r-bh r-rcpparmadillo)
optdepends=(r-covr r-ggplot2 r-knitr r-qgraph r-rmarkdown r-testthat)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_pkgver}.tar.gz")

build() {
  R CMD INSTALL ${_cranname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
}
sha256sums=('b3f2efc135d223c228012b9c4fb0cf910bad09786876723e5662c0090a9db4f2')
