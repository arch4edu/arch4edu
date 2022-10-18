# system requirements: A system installation of NLopt >= 2.4.0 (withheaders) will be used if available.
# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>

_pkgname=nloptr
_pkgver=2.0.3
pkgname=r-${_pkgname,,}
pkgver=2.0.3
pkgrel=6
pkgdesc='R Interface to NLopt'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('LGPL')
depends=(
  r
  nlopt
  r-testthat
)
optdepends=(
  r-inline
  r-knitr
  r-rmarkdown
  r-testthat
)
makedepends=(
  gcc-fortran
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('7b26ac1246fd1bd890817b0c3a145456c11aec98458b8518de863650b99616d7')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
