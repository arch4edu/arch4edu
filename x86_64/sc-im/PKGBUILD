# Maintainer: Shane Blackthorne <arch@blackthorne.dev>
# Contributor: TwoFinger <https://aur.archlinux.org/account/TwoFinger>
# Contributor: Rhinoceros <https://aur.archlinux.org/account/rhinoceros>

pkgname=sc-im
pkgver=0.8.5
pkgrel=1
pkgdesc='A ncurses vim-like terminal spreadsheet program, based on SC'
arch=('x86_64' 'i686' 'armv7h' 'aarch64')
url="https://github.com/andmarti1424/sc-im"
depends=('glibc' 'ncurses' 'gcc')
optdepends=('tmux: clipboard support'
	    'xclip: clipboard support'
	    'wl-clipboard: clipboard support'
            'gnuplot: create graphs'
	    'libxlsxwriter: export to xlsx. Requires rebuild of sc-im'
	    'python-xlsxwriter: for xlsx export support'
	    'libxml2: for xlsx import support'
	    'libzip: for ods import support'
	    'lua: for lua scripting')
license=('BSD-4-Clause')
conflicts=('sc-im-git')
source=("$pkgname-$pkgver.tar.gz::https://github.com/andmarti1424/$pkgname/archive/v${pkgver}.tar.gz"
        ${pkgname}_arch_0.8.4.patch)
sha256sums=('49adb76fc55bc3e6ea8ee414f41428db4aef947e247718d9210be8d14a6524bd'
            '2ba5a7c20d250d14a32dd3fad956779551cc18ab5f080ce149ba8395a70d0c41')

prepare() {
	cd "$pkgname-$pkgver/src"

	# patch to install in /usr instead of /usr/local (src/Makefile)
	patch < "$srcdir/${pkgname}_arch_0.8.4.patch"
	#patch -Np3 -i "${pkgname}_arch_0.8.4.patch"
}

build() {
	cd "$pkgname-$pkgver/src"

	#./configure --prefix=/usr
	CFLAGS="-fcommon -Wp,-D_FORTIFY_SOURCE=2" make CC=gcc
}

package() {
	cd "$pkgname-$pkgver/src"

	make DESTDIR="$pkgdir" install

	install -Dm644 "../LICENSE" "${pkgdir}/usr/share/licenses/$pkgname/LICENSE"
}
