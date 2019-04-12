# Maintainer: Jingbei Li <i@jingbei.li>
pkgdesc='A CUDA backend for Torch7'
pkgname='torch7-cutorch-git'
pkgver=r1026.5e9d86c
pkgrel=4
makedepends=('cmake' 'git')
depends=('torch7-git>=r819' 'cuda')
conflicts=('torch7-cutorch')
provides=('torch7-cutorch')
arch=('x86_64' 'i686')
url='https://github.com/torch/cutorch'
license=('BSD')
source=("${pkgname}::git+${url}" 'THCAtomics.cuh.patch')
sha512sums=('SKIP' '73de865f999774adeb55a11ff9354740373702276ebdc1b44a936f361254745241fafa856bb9b0973daa0246822ed6813cb443798e9d471feb774aafd3cfb5e9')

pkgver(){
	cd "${pkgname}"
	(
		set -o pipefail
		git describe --long 2>/dev/null | sed 's/\([^-]*-g\)/r\1/;s/-/./g' ||
		printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
	)
}

prepare(){
	cd "${pkgname}"

	# https://github.com/torch/cutorch/issues/834
	patch -p1 < "${srcdir}"/THCAtomics.cuh.patch
}

build(){
	CFLAGS="${CFLAGS/-fno-plt/}"
	CXXFLAGS="${CXXFLAGS/-fno-plt/}"

	cd "${pkgname}"
	CPATH=/usr/include/lua5.1 \
	cmake . -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Release
	make
}

package(){
	cd "${pkgname}"
	make DESTDIR="${pkgdir}" install

	# Move Lua C module
	mkdir -p "${pkgdir}/usr/lib/lua/5.1"
	mv "${pkgdir}/usr/lib/libcutorch.so" "${pkgdir}/usr/lib/lua/5.1/"

	# Move pure Lua modules
	mkdir -p "${pkgdir}/usr/share/lua/5.1"
	mv "${pkgdir}/usr/lua/cutorch" "${pkgdir}/usr/share/lua/5.1/"
	rm -rf "${pkgdir}/usr/lua"
}
