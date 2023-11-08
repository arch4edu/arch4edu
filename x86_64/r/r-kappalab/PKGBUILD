# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=kappalab
_pkgver=0.4-12
pkgname=r-${_pkgname,,}
pkgver=0.4.12
pkgrel=1
pkgdesc='Non-Additive Measure and Integral Manipulation Functions'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('CeCILL')
depends=(
  r
  r-lpsolve
  r-quadprog
  r-kernlab
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('b30829a18cc7ee3ee466edbbd6f85e3e41d445887e34eaf6a3fa58f53911138c')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
