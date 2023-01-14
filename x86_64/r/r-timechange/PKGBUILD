# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_cranname=timechange
_cranver=0.2.0
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="Efficient Manipulation of Date-Times"
arch=(i686 x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(GPL3)
depends=(cctz r)
makedepends=(r-cpp11)
checkdepends=(r-testthat)
optdepends=(r-testthat r-knitr)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
sha256sums=('3d602008052123daef94a5c3f5154c5461b4ec0432ab70c37273d7ddd252f7f1')

prepare() {
  # build against system cctz
  sed -i -e 's/$(SHLIB): libcctz.a/$(SHLIB):/' \
      -e 's#PKG_CPPFLAGS= -I. -I./cctz/src/#PKG_CPPFLAGS= -I.#' \
      "$_cranname/src/Makevars"
}

build() {
  mkdir -p build
  R CMD INSTALL "${_cranname}" -l "${srcdir}/build"
}

check() {
  cd "${_cranname}/tests"
  R_LIBS="${srcdir}/build" NOT_CRAN=true Rscript --vanilla testthat.R
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"

  cp -a --no-preserve=ownership "build/${_cranname}" "${pkgdir}/usr/lib/R/library"
}
