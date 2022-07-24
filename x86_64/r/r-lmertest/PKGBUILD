# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=lmerTest
_pkgver=3.1-3
pkgname=r-${_pkgname,,}
pkgver=3.1.3
pkgrel=3
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
sha256sums=('35aa75e9f5f2871398ff56a482b013e6828135ef04916ced7d1d7e35257ea8fd')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
