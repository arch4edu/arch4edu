# Maintainer: Jingbei Li <i@jingbei.li>
_cranname=mirt
_pkgver=1.48
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
sha256sums=('748dc043825630b302eabc483ec8a718de4552ccf53c21c1d6bad8cf0fcb0d28')
