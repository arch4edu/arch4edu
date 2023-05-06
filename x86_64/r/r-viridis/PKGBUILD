# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
_cranname=viridis
_cranver=0.6.3
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="Tools for Spatial Data"
arch=(i686 x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(MIT)
depends=('r>=2.10' 'r-viridislite>=0.4.0' 'r-ggplot2>=1.0.1' r-gridextra)
optdepends=(r-hexbin r-scales r-knitr r-dichromat r-colorspace r-httr r-mapproj r-vdiffr r-svglite r-testthat r-covr r-rmarkdown r-maps)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
sha512sums=('a4dd9f8d202e122c5f47ccd0ebc076effa89f5043fadfd68b57f9b1895867bf8ee162d82fee08ae9a9bb44ff33ba59e04f9a6ee6e52a78bdf966b3138ff23d3e')

build() {
  R CMD INSTALL ${_cranname}_${_cranver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"

  cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
}
