# Maintainer: Jingbei Li <i@jingbei.li>
_cranname=metaSEM
_pkgver=1.5.0
pkgname=r-metasem
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Meta-Analysis using Structural Equation Modeling"
arch=(x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(GPLv3)
depends=(r r-ellipse r-lavaan r-mvtnorm r-numderiv r-openmx)
makedepends=(gcc-fortran)
optdepends=(r-matrixcalc r-metafor r-r.rsp r-semplot r-testthat)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_pkgver}.tar.gz")

build() {
  R CMD INSTALL ${_cranname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
}
sha256sums=('356d9fe1cd1d83118d73a5ba6e7574e7894b7c50f50b8d5aacb2827a4cbc14b6')
