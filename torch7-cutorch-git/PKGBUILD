# Maintainer: Adrián Pérez de Castro <aperez@igalia.com>
pkgdesc='Neural networks package for Torch7'
pkgname='torch7-cutorch-git'
pkgver=r521.7d2a5d5
pkgrel=1
makedepends=('cmake' 'git')
depends=('torch7-git>=r819')
conflicts=('torch7-cutorch')
provides=('torch7-cutorch')
arch=('x86_64' 'i686')
url='https://github.com/torch/cutorch'
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
	cd "${pkgname}"
	cmake . -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Release
	make -j32
}

package () {
	cd "${pkgname}"
	make DESTDIR="${pkgdir}" install -j32

	# Move Lua C module
	mkdir -p "${pkgdir}/usr/lib/lua/5.1"
	mv "${pkgdir}/usr/lib/libcutorch.so" "${pkgdir}/usr/lib/lua/5.1/"

	# Move pure Lua modules
	mkdir -p "${pkgdir}/usr/share/lua/5.1"
	mv "${pkgdir}/usr/lua/cutorch" "${pkgdir}/usr/share/lua/5.1/"
	rm -rf "${pkgdir}/usr/lua"
}
