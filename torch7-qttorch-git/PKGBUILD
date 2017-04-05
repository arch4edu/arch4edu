# Maintainer: Stephen Zhang <zsrkmyn at gmail dot com>
pkgname='torch7-qttorch-git'
pkgdesc='qttorch in torch project'
pkgver=r18.ba5b5a1
pkgrel=1
url='https://github.com/torch/qttorch'
source=("${pkgname}::git+${url}.git")
depends=('luajit' 'torch7-qtlua')
optdepends=()
conflicts=('torch7-qttorch')
provides=('torch7-qttorch')
makedepends=('cmake' 'git')
arch=('x86_64' 'i686')
sha512sums=('SKIP')

pkgver () {
	cd "${pkgname}"
	(
		set -o pipefail
		git describe --long 2>/dev/null | sed 's/\([^-]*-g\)/r\1/;s/-/./g' ||
		printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
	)
}

prepare() {
	cd "${pkgname}"
	sed -i -e '6iFIND_PACKAGE(QtLua REQUIRED)' -e '8d' CMakeLists.txt
}

build () {
	cd "${pkgname}"
	cmake . \
		-DCMAKE_BUILD_TYPE=Release \
		-DCMAKE_INSTALL_PREFIX=/usr \
		-DLUA_BINDIR=/usr/bin \
		-DLUADIR=/usr/share/lua/5.1 \
		-DLUA_LIBDIR=/usr/lib/lua/5.1/ \
		-DLUALIB=/usr/lib/libluajit-5.1.so
	make
}

package () {
	cd "${pkgname}"
	make DESTDIR="${pkgdir}" install

	install -dm755 "${pkgdir}/usr/lib/lua/5.1"
	install -dm755 "${pkgdir}/usr/share/lua/5.1"
	mv "${pkgdir}/usr/lib/"*.so "${pkgdir}/usr/lib/lua/5.1/"
	mv "${pkgdir}/usr/lua/qttorch" "${pkgdir}/usr/share/lua/5.1/"
	rm -r "${pkgdir}/usr/lua"
}

