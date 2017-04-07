# Maintainer: Jingbei Li <i@jingbei.li>
# Contributor: Ziwei Zhu <zhuziwei1@outlook.com>
pkgdesc='deep extension to nn Modules and Criterions for Torch7'
pkgname='torch7-dpnn-git'
pkgver=r526.ca0e99f
pkgrel=1
makedepends=('cmake' 'git')
depends=('torch7-git' 'torch7-nn-git' 'torch7-nnx-git' 'lua-moses-git')
arch=('x86_64' 'i686')
url='https://github.com/Element-Research/dpnn'
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

	# Move pure Lua modules
	mkdir -p "${pkgdir}/usr/share/lua/5.1"
	mv "${pkgdir}/usr/lua/dpnn" "${pkgdir}/usr/share/lua/5.1/"
	rm -rf "${pkgdir}/usr/lua"
}
