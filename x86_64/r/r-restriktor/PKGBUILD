# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=restriktor
_pkgver=0.5-20
pkgname=r-${_pkgname,,}
pkgver=0.5.20
pkgrel=1
pkgdesc='Restricted Statistical Estimation and Inference for Linear Models'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-ggplot2
  r-ic.infer
  r-lavaan
  r-mvtnorm
  r-norm2
  r-quadprog
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('b43386d44da5938cfbc8b9c94256dcaa504bc1442b85bd32cdf7027e623c1091')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
