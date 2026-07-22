# Maintainer: Jingbei Li <i@jingbei.li>
_cranname=berryFunctions
_pkgver=1.22.13
pkgname=r-berryfunctions
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Function Collection Related to Plotting and Hydrology"
arch=(any)
url="https://cran.r-project.org/package=${_cranname}"
license=(GPLv3)
depends=(r r-abind)
optdepends=(r-knitr r-rmarkdown)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_pkgver}.tar.gz")

build() {
  R CMD INSTALL ${_cranname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
}
sha256sums=('a0f1d191622cc14c68e65100ed0e276975eb9960c8cdd4db18f18d167235df51')
