# Maintainer: DuckSoft <realducksoft@gmail.com>

_cranname=BAS
pkgname=r-bas
pkgver=1.6.4
pkgrel=1
pkgdesc="Bayesian Variable Selection and Model Averaging using Bayesian Adaptive Sampling"
arch=(x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(GPL3)
depends=(r)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${pkgver}.tar.gz")
sha256sums=('e517909f3896dad497507b6113ced7db03ad9ce3c97183b998ea06692e1bfef0')

build() {
  R CMD INSTALL ${_cranname}_${pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
}
