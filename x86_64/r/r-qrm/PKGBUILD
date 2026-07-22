# Maintainer: Jingbei Li <i@jingbei.li>
_cranname=QRM
_pkgver=0.4-35
pkgname=r-qrm
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Provides R-Language Functions to Examine Quantitative Risk Management Concepts"
arch=(x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(GPL-2)
depends=(r r-gsl r-mvtnorm r-numderiv r-rcpp r-timedate r-timeseries)
makedepends=(gcc-fortran)
optdepends=(r-knitr r-rmarkdown)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_pkgver}.tar.gz")

build() {
  R CMD INSTALL ${_cranname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
}
sha256sums=('327ff1acb478c0a47554c930ffd5c44ab9150e1617aea00b99f8b450c8956415')
