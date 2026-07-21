# Maintainer: Jingbei Li <i@jingbei.li>
_cranname=audio
_pkgver=0.1-12
pkgname=r-audio
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Audio Interface for R"
arch=(x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(MIT + file LICENSE)
depends=(r)
makedepends=(gcc-fortran)
optdepends=()
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_pkgver}.tar.gz")

build() {
  R CMD INSTALL ${_cranname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
  install -Dm644 "${_cranname}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
sha256sums=('bb358725f8758544202ca0da897f773848c9d2440ce2dbcfc76c69e03cae508e')
