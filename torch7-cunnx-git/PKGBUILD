# Maintainer: Jingbei Li <i@jingbei.lli>
pkgdesc='Experimental cuda nn package'
pkgname='torch7-cunnx-git'
pkgver=r185.3307c4a
pkgrel=1
makedepends=('cmake' 'git')
depends=('torch7-git>=r819' 'torch7-nn-git' 'torch7-cunn-git' 'torch7-nnx-git' 'torch7-cutorch-git' 'cuda')
conflicts=('torch7-cunnx')
provides=('torch7-cunnx')
arch=('x86_64' 'i686')
url='https://github.com/nicholas-leonard/cunnx'
license=('BSD')
source=("${pkgname}::git+${url}")
sha512sums=('SKIP')

pkgver () {
	cd "${pkgname}"
	(
	set -o pipefail
	git describe --long 2>/dev/null | sed 's/\([^-]*-g\)/r\1/;s/-/./g' ||
		printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
	)
}

build () {
	CFLAGS="${CFLAGS/-fno-plt/}"
	CXXFLAGS="${CFLAGS/-fno-plt/}"

	cd "${pkgname}"
	cmake . -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_CXX_COMPILER=g++-7 -DCMAKE_C_COMPILER=gcc-7 -DCMAKE_BUILD_TYPE=Release
	make
}

package () {
	cd "${pkgname}"
	make DESTDIR="${pkgdir}" install

	# Move Lua C module
	mkdir -p "${pkgdir}/usr/lib/lua/5.1"
	mv "${pkgdir}/usr/lib/libcunnx.so" "${pkgdir}/usr/lib/lua/5.1/"

	# Move pure Lua modules
	mkdir -p "${pkgdir}/usr/share/lua/5.1"
	mv "${pkgdir}/usr/lua/cunnx" "${pkgdir}/usr/share/lua/5.1/"
	rm -rf "${pkgdir}/usr/lua"
}
