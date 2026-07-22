# Maintainer: Jingbei Li <i@jingbei.li>
_cranname=mxsem
_pkgver=0.1.0
pkgname=r-mxsem
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Specify 'OpenMx' Models with a 'lavaan'-Style Syntax"
arch=(x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(GPLv3)
depends=(r r-dplyr r-openmx r-rcpp)
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
sha256sums=('a1825e0002b12b33ce14a1b3aa5bd44d1a0962063878cf54d34ff5f496451e56')
