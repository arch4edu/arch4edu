# Maintainer: AutoUpdateBot <auto_update_bot@arch4edu.org>
_cranname=charport
_pkgver=0.1.1
pkgname=r-charport
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="ALTREP String Interoperability"
arch=(x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(MIT)
depends=(r)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_pkgver}.tar.gz")
sha256sums=('9c48dd2aff4c977cd64bdda5dca746f550de679e0c25b33563636a07c90a2818')

build() {
  R CMD INSTALL ${_cranname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
}
