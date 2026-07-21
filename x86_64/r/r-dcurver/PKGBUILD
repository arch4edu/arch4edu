# Maintainer: Jingbei Li <i@jingbei.li>
_cranname=dcurver
_pkgver=0.9.3
pkgname=r-dcurver
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Utility Functions for Davidian Curves"
arch=(x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(GPLv3)
depends=(r r-rcpp r-rcpparmadillo)
makedepends=(gcc-fortran)
optdepends=(r-testthat)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_pkgver}.tar.gz")

build() {
  R CMD INSTALL ${_cranname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
}
sha256sums=('963a0e9af1c250a7e43e386823cc2d793c467c91a686c30df8058319e97355fc')
