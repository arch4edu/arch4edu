# Maintainer: Jingbei Li <i@jingbei.li>
_cranname=qs2
_pkgver=0.2.2
pkgname=r-qs2
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Efficient Serialization of R Objects"
arch=(x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(GPLv3)
depends=(r r-rcpp r-rcppparallel r-stringfish)
makedepends=(gcc-fortran)
optdepends=(r-data.table r-dplyr r-knitr r-rmarkdown r-stringi)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_pkgver}.tar.gz")

build() {
  R CMD INSTALL ${_cranname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
}
sha256sums=('c59ff879e858aef0afb13de25127239624e65b20179c8631fa1f62edea25f48f')
