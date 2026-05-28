# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=lmerTest
_pkgver=3.2-1
pkgname=r-${_pkgname,,}
pkgver=3.2.1
pkgrel=1
pkgdesc='Tests in Linear Mixed Effects Models'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-ggplot2
  r-lme4
  r-numderiv
)
optdepends=(
  r-pbkrtest
  r-tools
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('a0c5e6958940824fe09fc595383548e65ff08d3e363f4940e84a51084c025968')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
