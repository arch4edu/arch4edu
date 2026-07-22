# Maintainer: Jingbei Li <i@jingbei.li>
_cranname=rle
_pkgver=0.10.0
pkgname=r-rle
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Common Functions for Run-Length Encoded Vectors"
arch=(x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(GPLv3)
depends=(r)
makedepends=(gcc-fortran)
optdepends=(r-covr)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_pkgver}.tar.gz")

build() {
  R CMD INSTALL ${_cranname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
}
sha256sums=('191799a80f3a833dcad0ffe0e6ea73bfce3c1a7cd4c6e00839687a0e695834ab')
