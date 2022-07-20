# Maintainer: Robert Greener <me@r0bert.dev>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_cranname=R.methodsS3
_cranver=1.8.2
_updatedate=2022-06-25
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="S3 Methods Simplified"
arch=(any)
url="https://cran.r-project.org/package=${_cranname}"
license=(LGPL2.1 LGPL3)
depends=('r>=2.13.0')
source=("https://cran.microsoft.com/snapshot/${_updatedate}/src/contrib/${_cranname}_${_cranver}.tar.gz")
sha256sums=('822d5e61dad4c91e8883be2b38d7b89f87492046d0fe345704eb5d2658927c2e')

build() {
  R CMD INSTALL ${_cranname}_${_cranver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"

  cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
}
