# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=numbers
_pkgver=0.8-5
pkgname=r-${_pkgname,,}
pkgver=0.8.5
pkgrel=1
pkgdesc='Number-Theoretic Functions'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
optdepends=(
  r-gmp
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('77d5dedb7f953689ab9e89c14e673c0c8f644c8b392fab4ee4fb793930ad220b')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
