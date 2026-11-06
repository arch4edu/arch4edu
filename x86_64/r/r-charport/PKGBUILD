# Maintainer: AutoUpdateBot <auto_update_bot@arch4edu.org>
_cranname=charport
_pkgver=0.2.0
pkgname=r-charport
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="ALTREP String Interoperability"
arch=(x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(MIT)
depends=(r)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_pkgver}.tar.gz")
sha256sums=('3765851bc0a68dcaccb2fde79c7cb3c45bdee716fbce78dccc9e87a15302a6d3')

build() {
  R CMD INSTALL ${_cranname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
}
