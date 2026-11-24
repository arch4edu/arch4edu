# Maintainer: DuckSoft <realducksoft@gmail.com>

_cranname=BAS
pkgname=r-bas
pkgver=2.1.0
pkgrel=1
pkgdesc="Bayesian Variable Selection and Model Averaging using Bayesian Adaptive Sampling"
arch=(x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(GPL3)
depends=(r)
makedepends=(gcc-fortran)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${pkgver}.tar.gz")
sha256sums=('718408dcd0955c41d6ce3d92cb93c41737b41893f01a3008b69b7e42e4e1e94e')

build() {
  R CMD INSTALL ${_cranname}_${pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
}
