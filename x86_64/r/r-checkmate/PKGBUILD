# Maintainer: Robert Greener <me@r0bert.dev>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_cranname=checkmate
_cranver=2.1.0
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="Fast and Versatile Argument Checks"
arch=(i686 x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(BSD3)
depends=(
	"r>=3.0.0"
	"r-backports>=1.1.0"
)
checkdepends=(
	r-r6
	r-fastmatch
	"r-data.table>=1.9.8"
	r-devtools
	r-magrittr
	r-testthat
	r-tinytest
	r-tibble
)
optdepends=(
	r-ggplot2
	r-knitr
	r-microbenchmark
	r-rmarkdown
)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz"
	"CRANBSD::https://cran.r-project.org/web/licenses/BSD_3_clause")
sha512sums=("9ffe09baa5c6f928db7fcda935dfa344a374cf60c91b510968b20062e5f4abf415986d29b02a50195c0e08f3d9f0f77c29b13b5051c0c000d9144a364350d1cf"
	    "00a22b32654fd59818563612cf546c581c1f111826bdae43d9daae51bfedb185fd76769f7d7e4db255b38b6b9f3e380351a972bf7189279164eb3eb0fc873e36")

build() {
	mkdir -p build
	R CMD INSTALL ${_cranname}_${_cranver}.tar.gz -l "${srcdir}/build"
}

check() {
	cd "${_cranname}/tests"
	R_LIBS="${srcdir}/build" NOT_CRAN=true Rscript --vanilla test-all.R
}

package() {
	install -dm0755 "${pkgdir}/usr/lib/R/library"

	cp -a --no-preserve=ownership "build/${_cranname}" "${pkgdir}/usr/lib/R/library"
	install -Dm644 "${_cranname}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
	install -Dm644 CRANBSD "${pkgdir}/usr/share/licenses/${pkgname}/BSD_3_Clause"
}
