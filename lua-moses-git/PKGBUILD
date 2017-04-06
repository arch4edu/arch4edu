# Maintainer: Jingbei Li <i@jingbei.li>
pkgdesc="Utility library for functional programming in Lua"
pkgname='lua-moses-git'
pkgver=r261.d0b5c94
pkgrel=1
makedepends=('cmake' 'git')
depends=('lua')
arch=('x86_64' 'i686')
url='https://github.com/Yonaba/Moses'
license=('MIT')
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

package () {
	cd "${pkgname}"
	# Move pure Lua modules
	mkdir -p "${pkgdir}/usr/share/lua/5.1/moses"
	cp *.lua "${pkgdir}/usr/share/lua/5.1/moses"
}
