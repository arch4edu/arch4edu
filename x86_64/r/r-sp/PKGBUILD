_cranname=sp
_cranver=2.1-2
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="Classes and Methods for Spatial Data"
arch=(i686 x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(GPL2 GPL3)
depends=('r>=3.2.0')
optdepends=(r-rcolorbrewer r-rgdal r-rgeos r-gstat r-maptools r-deldir r-knitr r-rmarkdown)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
sha256sums=('bfdbb4a62f9fe0c554f88c75af6f214dc9a550da09bd3aefe1115ac6963e0dc5')

build() {
  R CMD INSTALL ${_cranname}_${_cranver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"

  cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
}
