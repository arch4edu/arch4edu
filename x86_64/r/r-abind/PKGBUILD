# Maintainer: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Taekyung Kim <Taekyung.Kim.Maths@gmail.com>
# Contributor: Alex Branham <branham@utexas.edu>

_cranname=abind
_cranver=1.4-5
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="Combine Multidimensional Arrays"
arch=(any)
url="https://cran.r-project.org/package=${_cranname}"
license=(LGPL2 LGPL2.1 LGPL3)
depends=('r>=1.5.0')
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
sha256sums=('3a3ace5afbcb86e56889efcebf3bf5c3bb042a282ba7cc4412d450bb246a3f2c')

build() {
  R CMD INSTALL ${_cranname}_${_cranver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"

  cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
}
