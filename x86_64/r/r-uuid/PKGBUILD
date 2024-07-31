# Maintainer: Alex Hirzel <alex at hirzel period us>
# Contributor: Pranav K Anupam <pranavanupam@yahoo.com>

_cranname=uuid
_cranver=1.2-1
_pkgtar=${_cranname}_${_cranver}.tar.gz
pkgname=r-uuid
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="Tools for generating and handling of UUIDs (Universally Unique Identifiers)."
arch=('any')
url="https://cran.r-project.org/package=${_cranname}"
license=('MIT')
depends=('r>=2.9.0')
optdepends=('r-bigReg')

source=("https://cran.r-project.org/src/contrib/${_pkgtar}")
sha256sums=('f90e49733d7d6ea7cf91abdc07b7d0e9a34a4b993e6914d754f0621281fc4b96')

build() {
	cd "${srcdir}"
	R CMD INSTALL ${_pkgtar} -l ${srcdir}
}
package() {
	cd "${scrdir}"
	install -dm0755 "$pkgdir/usr/lib/R/library"

	# TODO - this does not include the MIT terms themselves, which are not
	# actually distributed with the package, and this case is not covered by the
	# wiki yet: <https://wiki.archlinux.org/title/R_package_guidelines>
	install -Dm644 "${_cranname}/LICENSE" -t "${pkgdir}/usr/share/licenses/$pkgname"

	cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
}
