# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=optimx
_pkgver=2022-4.30
pkgname=r-${_pkgname,,}
pkgver=2022.4.30
pkgrel=1
pkgdesc="Expanded Replacement and Extension of the 'optim' Function"
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-numderiv
)
optdepends=(
  r-bb
  r-dfoptim
  r-knitr
  r-lbfgs
  r-lbfgsb3c
  r-minqa
  r-rmarkdown
  r-setrng
  r-subplex
  r-ucminf
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('ebe9887a22296cf4b2db07981aaa1f898bf7c17fb61a4b398c228d4077d0b410')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
