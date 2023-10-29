# Maintainer: Alex Hirzel <alex at hirzel period us>
# Contributor: Pranav K Anupam <pranavanupam@yahoo.com>

_cranname=uuid
_cranver=1.1-1
_pkgtar=${_cranname}_${_cranver}.tar.gz
pkgname=r-uuid
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="Tools for generating and handling of UUIDs (Universally Unique Identifiers)."
arch=('any')
url="https://cran.r-project.org/package=${_cranname}"
license=('GPL3')
depends=('r>=2.9.0')
optdepends=('r-bigReg')

source=("https://cran.r-project.org/src/contrib/${_pkgtar}")
sha256sums=('1611240eb706e6f53400b25c9cf792ad90f151b72ed0918a1e756997f7abb716')

build() {
	cd "${srcdir}"
	R CMD INSTALL ${_pkgtar} -l ${srcdir}
}
package() {
	cd "${scrdir}"
	install -dm0755 "$pkgdir/usr/lib/R/library"
	cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
}
