# Maintainer: Robert Greener <me@r0bert.dev>
_cranname=brio
_cranver=1.1.3
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=2
pkgdesc="Basic R Input Output"
arch=(x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(MIT)
depends=(
	r
)
checkdepends=(
	r-testthat
)
optdepends=(
	r-covr
)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz"
	"CRAN_MIT::https://cran.r-project.org/web/licenses/MIT")

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

	mkdir -p "${pkgdir}/usr/share/licenses/${pkgname}"
	cp -a --no-preserve=ownership "${_cranname}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
	cp CRAN_MIT "${pkgdir}/usr/share/licenses/${pkgname}/MIT"
}

sha256sums=('eaa89041856189bee545bf1c42c7920a0bb0f1f70bb477487c467ee3e8fedcc6'
            'e76e4aad5d3d9d606db6f8c460311b6424ebadfce13f5322e9bae9d49cc6090b')
