# Maintainer: Jingbei Li <i@jingbei.li>
_cranname=glassoFast
_pkgver=1.0.1
pkgname=r-glassofast
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Fast Graphical LASSO"
arch=(x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(GPLv3)
depends=(r)
makedepends=(gcc-fortran)
optdepends=(r-glasso r-rbenchmark)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_pkgver}.tar.gz")

build() {
  R CMD INSTALL ${_cranname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
}
sha256sums=('ffc340420d7693af4e361811fb8cf593083c2c341b07376b902533c373addb5b')
