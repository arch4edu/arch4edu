# Maintainer: DuckSoft <realducksoft@gmail.com>

_cranname=SEMsens
pkgname=r-semsens
pkgver=1.5.5
pkgrel=1
pkgdesc="Bayesian Variable Selection and Model Averaging using Bayesian Adaptive Sampling"
arch=(x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(GPL3)
depends=(r r-lavaan r-stats)
makedepends=(gcc-fortran)
optdepends=(r-knitr r-rmarkdown)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${pkgver}.tar.gz")
sha256sums=('ee15d80ea05f1a031fb907f821f8dee9d5163c415a9c056858a22ed93b3aec49')

build() {
  R CMD INSTALL ${_cranname}_${pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
}
