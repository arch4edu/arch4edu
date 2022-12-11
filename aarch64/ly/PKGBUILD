# Maintainer: éclairevoyant
# Contributor: nullgemm <nullgemm@mailbox.org>

pkgname=ly
pkgver=0.5.3
pkgrel=2
pkgdesc="TUI display manager"
arch=('i686' 'x86_64' 'aarch64')
url="https://github.com/fairyglade/$pkgname"
license=('custom:WTFPL')
makedepends=('git')
depends=('pam' 'xorg-xauth')
conflicts=('python-ly') # TODO prevent this
backup=(etc/$pkgname/{config.ini,wsetup.sh,xsetup.sh})
source=("git+$url.git#tag=v$pkgver"
        "git+https://github.com/nullgemm/argoat.git"
        "git+https://github.com/nullgemm/configator.git"
        "git+https://github.com/nullgemm/dragonfail.git"
        "git+https://github.com/nullgemm/termbox_next.git")
b2sums=('SKIP'
        'SKIP'
        'SKIP'
        'SKIP'
        'SKIP')

prepare() {
	cd $pkgname
	git submodule init
	for _i in argoat configator dragonfail termbox_next; do
		git config submodule.sub/$_i.url "$srcdir/$_i"
	done
	git -c protocol.file.allow=always submodule update
}

build() {
	make -C $pkgname
}

package() {
	cd $pkgname
	make DESTDIR="$pkgdir" install
	install -Dm644 license.md "$pkgdir/usr/share/licenses/$pkgname/WTFPL"
}
