# Maintainer: Robert Greener <me@r0bert.dev>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_cranname=loo
_cranver=2.5.1
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="Efficient Leave-One-Out Cross-Validation and WAIC for Bayesian Models"
arch=(any)
url="https://cran.r-project.org/package=${_cranname}"
license=(GPL3)
depends=(
	"r>=3.1.2"
	r-checkmate
	"r-matrixstats>=0.52"
	"pandoc>=1.12.3"
	haskell-citeproc
)
checkdepends=(
	r-rstan
	r-testthat
)
optdepends=(
	r-bayesplot
	r-brms
	r-ggplot2
	r-knitr
	r-rmarkdown
	r-rstan
	r-rstanarm
	r-rstantools
	r-spdep
	r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
b2sums=("a4399fa44ff5387087f3737890daf9d3507c6e07d4f765d0b722188b8716703b2e7f0481246782675c37bc69afa0f460a8839a771e66866823f02c53fef4c2d6")

build() {
	mkdir -p build
	R CMD INSTALL ${_cranname}_${_cranver}.tar.gz -l "${srcdir}/build"
}

check() {
	cd "${_cranname}/tests"
	R_LIBS="${srcdir}/build" NOT_CRAN=true Rscript --vanilla testthat.R
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"

  cp -a --no-preserve=ownership "build/${_cranname}" "${pkgdir}/usr/lib/R/library"
}
