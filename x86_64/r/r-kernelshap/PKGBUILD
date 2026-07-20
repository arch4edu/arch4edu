# Maintainer: Jingbei Li <i@jingbei.li>
_cranname=kernelshap
_pkgver=0.9.1
pkgname=r-kernelshap
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Kernel SHAP"
arch=(x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(GPLv3)
depends=(r r-dofuture r-foreach)
makedepends=(gcc-fortran)
optdepends=(r-testthat)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_pkgver}.tar.gz")

build() {
  R CMD INSTALL ${_cranname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
}
sha256sums=('40bf27daf89d10771e2541853baa56377455141b5187186cf239878f268b359c')
