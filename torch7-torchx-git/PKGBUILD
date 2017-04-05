# Maintainer: Jingbei Li <i@jingbei.li>
# Contributor: Ziwei Zhu <zhuziwei1@outlook.com>
pkgdesc='torch extensions'
pkgname='torch7-torchx-git'
pkgver=r61.06cdbd3
pkgrel=1
makedepends=('cmake' 'git')
depends=('torch7-git' 'torch7-paths-git' 'torch7-sys-git')
arch=('x86_64' 'i686')
url='git://github.com/nicholas-leonard/torchx'
license=('BSD')
source=("${pkgname}::git+${url}")
md5sums=('SKIP')

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
	make
}

package () {
	cd "${pkgname}"
	make DESTDIR="${pkgdir}" install

	# Move Lua C module
	#mkdir -p "${pkgdir}/usr/lib/lua/5.1"
	#mv "${pkgdir}/usr/lib/libTHNN.so" "${pkgdir}/usr/lib/lua/5.1/"

	# Move pure Lua modules
	mkdir -p "${pkgdir}/usr/share/lua/5.1"
	mv "${pkgdir}/usr/lua/torchx" "${pkgdir}/usr/share/lua/5.1/"
	rm -rf "${pkgdir}/usr/lua"
}
