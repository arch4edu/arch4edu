# Maintainer: Jingbei Li <i@jingbei.li>
_cranname=Bergm
_pkgver=5.0.7
pkgname=r-bergm
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Bayesian Exponential Random Graph Models"
arch=(x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(GPLv3)
depends=(r r-coda r-ergm r-matrixcalc r-mcmcpack r-mvtnorm r-network r-rglpk r-statnet.common)
makedepends=(gcc-fortran)
optdepends=(r-spelling)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_pkgver}.tar.gz")

build() {
  R CMD INSTALL ${_cranname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
}
sha256sums=('391aea0d052126ac3dff4d7eddde41329d4fdca46ba3791d9a6d486ce59a8d8f')
