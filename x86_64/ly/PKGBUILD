# Maintainer: nullgemm <nullgemm@mailbox.org>
pkgname=ly
pkgver=0.5.3
pkgrel=0
pkgdesc="TUI display manager"
arch=('i686' 'x86_64' 'aarch64')
url="https://github.com/nullgemm/ly"
license=('custom:WTFPL')
makedepends=('git')
depends=('pam' 'xorg-xauth')
conflicts=('ly-git' 'python-ly-git')
backup=('etc/ly/config.ini')
source=("git+https://github.com/nullgemm/${pkgname}.git#tag=v${pkgver}"
        "git+https://github.com/nullgemm/argoat.git"
        "git+https://github.com/nullgemm/configator.git"
        "git+https://github.com/nullgemm/dragonfail.git"
        "git+https://github.com/nullgemm/termbox_next.git")
sha256sums=('SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP')

prepare() {
	cd "$srcdir/$pkgname"
	git submodule init
	for _i in argoat configator dragonfail termbox_next; do
		git config submodule.sub/${_i}.url $srcdir/${_i}
	done
	git submodule update
}

build() {
	cd "$srcdir/$pkgname"
	make
}

package() {
	cd "$srcdir/$pkgname" 
	make DESTDIR="$pkgdir" install
	install -Dm644 license.md "${pkgdir}/usr/share/licenses/${pkgname}/WTFPL"
}
