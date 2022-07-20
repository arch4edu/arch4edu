# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Taekyung Kim <Taekyung.Kim.Maths@gmail.com>
# Contributor: Ward Segers <w@rdsegers.be>
# Contributor: Alex Branham <branham@utexas.edu>

_cranname=quantreg
_cranver=5.93
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="Quantile Regression"
arch=(i686 x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(GPL)
depends=(r-sparsem r-matrixmodels)
makedepends=(gcc-fortran)
optdepends=(
    r-tripack
    r-akima
    r-rgl
    r-logspline
    r-nor1mix
    r-formula
    r-zoo
    r-r.rsp
    r-conquer
)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
sha256sums=('d4a94984a500bf4c92dec21013441f001a4aa0541c4c651384e257a4b4e9e539')

build() {
  mkdir -p build
  R CMD INSTALL "${_cranname}" -l "${srcdir}/build"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"

  cp -a --no-preserve=ownership "build/${_cranname}" "${pkgdir}/usr/lib/R/library"
}
