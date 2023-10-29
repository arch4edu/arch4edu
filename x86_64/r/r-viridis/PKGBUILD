# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
_cranname=viridis
_cranver=0.6.4
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
sha512sums=('61cba660e79b0c67430c585fc7af9a20b0cbb163ac99f5e61314a1eef87ff9bc40a866a94fc56ceba4fc73be91e95fa923037e7707aa4a592612d7e709ed16f2')

build() {
  R CMD INSTALL ${_cranname}_${_cranver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"

  cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
}
