# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=weights
_pkgver=1.0.4
pkgname=r-${_pkgname,,}
pkgver=1.0.4
pkgrel=4
pkgdesc='Weighting and Weighted Statistics'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-gdata
  r-hmisc
  r-lme4
  r-mice
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('efbe65e8a9d05824a86095d45ed62ce24d82101d4ca3b94828d443e08e83ccba')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
