# Maintainer: Jingbei Li <i@jingbei.li>
_cranname=nanonext
_pkgver=1.10.3
pkgname=r-nanonext
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Lightweight Toolkit for Messaging, Concurrency and the Web"
arch=(x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(MIT + file LICENSE)
depends=(r)
makedepends=(gcc-fortran)
optdepends=(r-later r-litedown)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_pkgver}.tar.gz")

build() {
  R CMD INSTALL ${_cranname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
  install -Dm644 "${_cranname}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
sha256sums=('f025e956a290798b072ea21de68ce315f3e3d993ea95ff3a6f14e301bcffb4c5')
