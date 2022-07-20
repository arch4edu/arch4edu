# Maintainer: Robert Greener <me@r0bert.dev>
_cranname=gdtools
_cranver=0.2.4
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="Utilities for Graphical Rendering"
arch=(any)
url="https://cran.r-project.org/package=${_cranname}"
license=(GPL3)
depends=(
	cairo
	fontconfig
	freetype2
	r
	r-rcpp
	r-systemfonts
)
checkdepends=(
	r-htmltools
	r-testthat
	r-fontquiver
	r-curl
)
optdepends=(
	r-htmltools
	r-testthat
	r-fontquiver
	r-curl
)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")

build() {
	mkdir -p build
	R CMD INSTALL "${_cranname}" -l "${srcdir}/build"
}

check() {
	if [ -d "${_cranname}/tests" ]
	then
  		cd "${_cranname}/tests"
		for i in *.R; do
			R_LIBS="${srcdir}/build" Rscript --vanilla $i
		done
	fi
}

package() {
	install -dm0755 "${pkgdir}/usr/lib/R/library"

	cp -a --no-preserve=ownership "build/${_cranname}" "${pkgdir}/usr/lib/R/library"
}

sha256sums=('32884ce1aa49be1fd897b4f808cdbc8727cb0d881ff8961e899220b2cac33028')
