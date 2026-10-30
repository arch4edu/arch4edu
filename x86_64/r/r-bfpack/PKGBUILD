# Maintainer: Jingbei Li <i@jingbei.li>
_cranname=BFpack
_pkgver=1.6.3
pkgname=r-bfpack
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Flexible Bayes Factor Testing of Scientific Expectations"
arch=(x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(GPLv3)
depends=(r r-bain r-bergm r-berryfunctions r-coda r-ergm r-lme4 r-metabma r-mvtnorm r-pracma r-qrm r-sandwich)
makedepends=(gcc-fortran)
optdepends=(r-knitr r-lmtest r-metafor r-polycor r-pscl r-remstimate r-rmarkdown r-testthat)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_pkgver}.tar.gz")
sha256sums=('7cde2b429c7c684a7f69b131d7b2226dc065f52524b5b46790ed53045678b660')

build() {
  R CMD INSTALL ${_cranname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
}
