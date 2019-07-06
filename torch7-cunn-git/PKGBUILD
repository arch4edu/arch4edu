# Maintainer: Frantic1048 <archer@frantic1048.com>
pkgdesc='CUDA backend for Torch7 Neural Network Package'
pkgname='torch7-cunn-git'
pkgver=r819.1ae6aa0
pkgrel=5
makedepends=('cmake' 'git')
depends=('torch7-git>=r819' 'cuda' 'torch7-nn-git' 'torch7-cutorch-git')
conflicts=('torch7-cunn')
provides=('torch7-cunn')
arch=('x86_64' 'i686')
url='https://github.com/torch/cunn'
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

prepare() {
	cd "${pkgname}"

	# https://stackoverflow.com/questions/46345811/cuda-9-shfl-vs-shfl-sync
	sed -e 's/__shfl(/__shfl_sync(0xFFFFFFFF, /g' -e 's/__any(/__any_sync(0xFFFFFFFF, /g' -i lib/THCUNN/LookupTable.cu
}

build () {
	CFLAGS="${CFLAGS/-fno-plt/}"
	CXXFLAGS="${CFLAGS/-fno-plt/}"

	cd "${pkgname}"
	cmake . -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_C_COMPILER=gcc-8 -DCMAKE_BUILD_TYPE=Release
	make
}

package () {
	cd "${pkgname}"
	make DESTDIR="${pkgdir}" install

	# Move Lua C module
	mkdir -p "${pkgdir}/usr/lib/lua/5.1"
	mv "${pkgdir}/usr/lib/libTHCUNN.so" "${pkgdir}/usr/lib/lua/5.1/"

	# Move pure Lua modules
	mkdir -p "${pkgdir}/usr/share/lua/5.1"
	mv "${pkgdir}/usr/lua/cunn" "${pkgdir}/usr/share/lua/5.1/"
	rm -rf "${pkgdir}/usr/lua"
}
