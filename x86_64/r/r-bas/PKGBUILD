# Maintainer: DuckSoft <realducksoft@gmail.com>

_cranname=BAS
pkgname=r-bas
pkgver=1.6.3
pkgrel=1
pkgdesc="Bayesian Variable Selection and Model Averaging using Bayesian Adaptive Sampling"
arch=(x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(GPL3)
depends=(r)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${pkgver}.tar.gz")
sha256sums=('59d28e381465dd487061799df8fb374d2e9a950237730eb8aad2071ce20ffd50')

build() {
  R CMD INSTALL ${_cranname}_${pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
}
