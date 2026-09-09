# Maintainer: Jingbei Li <i@jingbei.li>
_cranname=nanonext
_pkgver=1.10.2
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
sha256sums=('bcfe6bae45ced1cb3a9105f35addd5645b71a142096fc8870b0befc75d3b7856')
