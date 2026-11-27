# Maintainer: AutoUpdateBot <auto_update_bot@arch4edu.org>
_cranname=charport
_pkgver=0.3.0
pkgname=r-charport
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="ALTREP String Interoperability"
arch=(x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(MIT)
depends=(r)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_pkgver}.tar.gz")
sha256sums=('033a3214d4721c4f3707bffd8bbace207190c4249eb0d661a83cb6586b72847d')

build() {
  R CMD INSTALL ${_cranname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
}
