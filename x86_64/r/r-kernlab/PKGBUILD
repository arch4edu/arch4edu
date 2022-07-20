# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Alex Branham <branham@utexas.edu>

_cranname=kernlab
_cranver=0.9-31
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="Kernel-Based Machine Learning Lab"
arch=(i686 x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(GPL2)
depends=(r)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
sha256sums=('7359c665c1c5e6780e1ce44b143347c8eec839301c3079d7f19e29159873278a')

build() {
  mkdir -p build
  R CMD INSTALL "${_cranname}" -l "${srcdir}/build"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"

  cp -a --no-preserve=ownership "build/${_cranname}" "${pkgdir}/usr/lib/R/library"
}
