# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Alex Branham <alex.branham@gmail.com>

_cranname=robustbase
_cranver=0.95-0
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="Basic Robust Statistics"
arch=(i686 x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(GPL)
depends=(r-deoptimr)
makedepends=(gcc-fortran)
optdepends=(
    r-robust
    r-fit.models
    r-mpv
    r-xtable
    r-ggplot2
    r-ggally
    r-rcolorbrewer
    r-reshape2
    r-sfsmisc
    r-catdata
    r-doparallel
    r-foreach
    r-skewt
)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
sha256sums=('5cfaea1c46df6d45086614fea5f152c8da8ebfcadf33bb8df5b82e742eef9724')

build() {
  mkdir -p build
  R CMD INSTALL "${_cranname}" -l "${srcdir}/build"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"

  cp -a --no-preserve=ownership "build/${_cranname}" "${pkgdir}/usr/lib/R/library"
}
