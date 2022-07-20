# Maintainer: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Matt Frichtl <frichtlm@gmail.com>
# Contributor: wagnerflo <florian@wagner-flo.net>

_cranname=lazyeval
_cranver=0.2.2
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="Lazy (Non-Standard) Evaluation"
arch=(i686 x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(GPL3)
depends=('r>=3.1.0')
optdepends=(r-knitr r-rmarkdown r-testthat r-covr)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
sha256sums=('d6904112a21056222cfcd5eb8175a78aa063afe648a562d9c42c6b960a8820d4')

build() {
  R CMD INSTALL ${_cranname}_${_cranver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"

  cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
}
