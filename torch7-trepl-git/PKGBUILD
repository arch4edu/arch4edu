# Maintainer: Adrián Pérez de Castro <aperez@igalia.com>
pkgdesc='A REPL for Torch'
pkgname='torch7-trepl-git'
pkgver=r158.06128f9
pkgrel=1
depends=('torch7-git' 'lua51-penlight')
makedepends=('git')
conflicts=('torch7-trepl')
provides=('torch7-trepl')
arch=('x86_64' 'i686')
url='https://github.com/torch/trepl'
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
	echo "Building: readline.so"
	gcc -shared -fPIC -I/usr/include/luajit-2.0 -o readline.so readline.c -lluajit-5.1 -lreadline
	echo "Building: treplutils.so"
	gcc -shared -fPIC -I/usr/include/luajit-2.0 -o treplutils.so utils.c -lluajit-5.1
}

package () {
	cd "${pkgname}"
	for name in readline treplutils ; do
		install -Dm755 "${name}.so" "${pkgdir}/usr/lib/lua/5.1/${name}.so"
	done
	for name in init colors colorize ; do
		install -Dm644 "${name}.lua" "${pkgdir}/usr/share/lua/5.1/trepl/${name}.lua"
	done
	install -Dm755 th "${pkgdir}/usr/bin/th"
}
