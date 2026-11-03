# Maintainer: Jingbei Li <i@jingbei.li>
_cranname=qs2
_pkgver=0.4.0
pkgname=r-qs2
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Efficient Serialization of R Objects"
arch=(x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(GPLv3)
depends=(r r-charport r-rcpp r-rcppparallel)
makedepends=(gcc-fortran)
optdepends=(r-data.table r-dplyr r-knitr r-rmarkdown r-stringi)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_pkgver}.tar.gz")

build() {
  R CMD INSTALL ${_cranname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
}
sha256sums=('9ab39bcaca5bfc2b56420ca155d48a05a06a273fbcf77290b65799d8e8dee351')
