# Maintainer: Jingbei Li <i@jingbei.li>
_cranname=Bergm
_pkgver=6.0.0
pkgname=r-bergm
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Bayesian Exponential Random Graph Models"
arch=(x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(GPLv3)
depends=(r r-coda r-ergm r-mice r-network r-rcpp)
optdepends=(r-spelling)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_pkgver}.tar.gz")

build() {
  R CMD INSTALL ${_cranname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
}
sha256sums=('d68b2576a61f0f2d5a101a5ce0f8ab83ac0a22234001efcd9c56027b5531d8c2')
