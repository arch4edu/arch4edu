# Maintainer: Jingbei Li <i@jingbei.li>
_cranname=mantar
_pkgver=0.3.2
pkgname=r-mantar
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Missingness Alleviation for Network Analysis"
arch=(x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(GPLv3)
depends=(r r-glassofast r-mathjaxr r-rdpack)
makedepends=(gcc-fortran)
optdepends=(r-knitr r-lavaan r-mice r-numderiv r-qgraph r-rmarkdown r-testthat)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_pkgver}.tar.gz")

build() {
  R CMD INSTALL ${_cranname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
}
sha256sums=('1237c20756e60ba4785fca708ad05b1b0d0f2b5521fceb6624a0248cb5886172')
