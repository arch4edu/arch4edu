# Maintainer: Jingbei Li <i@jingbei.li>
# Contributor: Ziwei Zhu <zhuziwei1@outlook.com>
pkgdesc="Recurrent Neural Network library for Torch7's nn"
pkgname='torch7-rnn-git'
pkgver=r567.ccaf7af
pkgrel=1
makedepends=('cmake' 'git')
depends=('torch7-cunnx-git' 'torch7-dpnn-git' 'torch7-git' 'torch7-nn-git' 'torch7-nnx-git' 'torch7-torchx-git')
arch=('x86_64' 'i686')
url='https://github.com/Element-Research/rnn'
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
	mv "${pkgdir}/usr/lua/rnn" "${pkgdir}/usr/share/lua/5.1/"
	rm -rf "${pkgdir}/usr/lua"
}
