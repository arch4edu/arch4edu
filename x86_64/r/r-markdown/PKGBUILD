# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Kibouo <csonka.mihaly@hotmail.com>
# Contributor: Alex Branham <branham@utexas.edu>

_cranname=markdown
_cranver=1.6
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="Render Markdown with 'commonmark'"
arch=(any)
url="https://cran.r-project.org/package=${_cranname}"
license=(GPL2)
depends=(r-commonmark r-xfun)
optdepends=(
    r-knitr
    r-rmarkdown
    r-yaml
    r-rcurl
)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
sha256sums=('46228b8d8161ae4b651b4662364eb35a3b91e6a7a457fe99d0e709f2a6f559ea')

build() {
  mkdir -p build
  R CMD INSTALL "${_cranname}" -l "${srcdir}/build"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"

  cp -a --no-preserve=ownership "build/${_cranname}" "${pkgdir}/usr/lib/R/library"
}
