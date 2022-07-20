# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_cranname=remotes
_cranver=2.4.2
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="R Package Installation from Remote Repositories, Including 'GitHub'"
arch=(any)
url="https://cran.r-project.org/package=${_cranname}"
license=(MIT)
depends=('r>=3.0.0' subversion git)
optdepends=(r-brew r-callr r-curl r-covr r-git2r r-knitr r-mockery r-pkgbuild r-pingr r-rmarkdown r-rprojroot r-testthat r-webfakes r-withr)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
sha256sums=('f2ef875f24a485bf4f55a8c830f87cdd5db868f9a8cdb624dc452d0bf66ba516')

build() {
  R CMD INSTALL ${_cranname}_${_cranver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"

  cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
}
