# Maintainer: Jingbei Li <i@jingbei.li>

pkgname=vim-disable-mouse
pkgver=r1.12557b4
pkgrel=1
pkgdesc='Disable mouse in Vim'
url="https://github.com/petronny/${pkgname}"
arch=('any')
license=('GPL3')
depends=('vim')
makedepends=('git')
source=("git+${url}")
sha512sums=('SKIP')

pkgver() {
	cd "${pkgname}"
	printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

package() {
	cd "${srcdir}/${pkgname}"
	install -Dm644 plugin/disable-mouse.vim "$pkgdir/usr/share/vim/vimfiles/plugin/disable-mouse.vim"
}
