# Maintainer: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_cranname=viridis
_cranver=0.6.2
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="Tools for Spatial Data"
arch=(i686 x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(MIT)
depends=('r>=2.10' 'r-viridislite>=0.4.0' 'r-ggplot2>=1.0.1' r-gridextra)
optdepends=(r-hexbin r-scales r-knitr r-dichromat r-colorspace r-raster r-rastervis r-httr r-mapproj r-vdiffr r-svglite r-testthat r-covr r-rmarkdown r-rgdal r-maps)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
sha256sums=('69b58cd1d992710a08b0b227fd0a9590430eea3ed4858099412f910617e41311')

build() {
  R CMD INSTALL ${_cranname}_${_cranver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"

  cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
}
