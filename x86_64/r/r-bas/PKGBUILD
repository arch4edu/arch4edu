# Maintainer: DuckSoft <realducksoft@gmail.com>

_cranname=BAS
pkgname=r-bas
pkgver=1.6.2
pkgrel=1
pkgdesc="Bayesian Variable Selection and Model Averaging using Bayesian Adaptive Sampling"
arch=(x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(GPL3)
depends=(r)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${pkgver}.tar.gz")
sha256sums=('ecfc7f93d4d92d2c7c4dd72cee9b4843999e3b83ed64d46b207eca57d1931a35')

build() {
  R CMD INSTALL ${_cranname}_${pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
}
