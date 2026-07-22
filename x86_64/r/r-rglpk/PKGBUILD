# Maintainer: Jingbei Li <i@jingbei.li>
_cranname=Rglpk
_pkgver=0.6-5.1
pkgname=r-rglpk
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="R/GNU Linear Programming Kit Interface"
arch=(x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(GPL-2 GPL-3)
depends=(r r-slam glpk)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_pkgver}.tar.gz")

build() {
  R CMD INSTALL ${_cranname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
}
sha256sums=('e528b8c487e9dfef16ade3b834a17fc93cc898869978a5dd79bee2c5bf9cb6c9')
