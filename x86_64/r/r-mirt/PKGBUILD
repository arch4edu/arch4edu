# Maintainer: Jingbei Li <i@jingbei.li>
_cranname=mirt
_pkgver=1.47
pkgname=r-mirt
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Multidimensional Item Response Theory"
arch=(x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(GPLv3)
depends=(r r-gparotation r-gridextra r-rcpp r-vegan r-deriv r-splines2 r-pbapply r-dcurver r-simdesign)
makedepends=(gcc-fortran)
optdepends=(r-boot r-mirai r-latticeextra r-directlabels r-shiny r-knitr r-markdown r-rsolnp r-nloptr r-sirt r-plink r-mirtCAT r-testthat)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_pkgver}.tar.gz")

build() {
  R CMD INSTALL ${_cranname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
}
sha256sums=('f92727cdc00af8f0bf9d530480f80a88696682008ac36ff22829edf9d452472a')
