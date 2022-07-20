# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=jfa
_pkgver=0.6.4
pkgname=r-${_pkgname,,}
pkgver=0.6.4
pkgrel=1
pkgdesc='Bayesian and Classical Audit Sampling'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-extradistr
)
optdepends=(
  r-kableextra
  r-knitr
  r-mus
  r-rmarkdown
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('8237a0d4dfb04a71696bd9123c6c173209a945aa91e9b602943027c8b22457cf')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
