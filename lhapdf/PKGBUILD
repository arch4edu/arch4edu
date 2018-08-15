# Maintainer: Frank Siegert <frank.siegert@googlemail.com>
# Contributor: JP-Ellis <josh@jpellis.me>
pkgname=lhapdf
pkgver=6.2.1
pkgrel=4
pkgdesc="A particle physics tool for evaluating PDFs from discretised data files."
arch=('x86_64' 'i686')
url="http://lhapdf.hepforge.org/"
license=('GPL3')
depends=('python')
optdepends=('python2')
makedepends=(cython)
install=lhapdf.install
source=("http://www.hepforge.org/archive/lhapdf/LHAPDF-$pkgver.tar.gz")
noextract=()
md5sums=('9e05567d538fdb4862d4781cd076d7db')

prepare() {
        cd "$srcdir/LHAPDF-$pkgver"
        sed -e 's/print Cython.Compiler.Version.version/print (Cython.Compiler.Version.version)/g' -i m4/cython.m4
        autoreconf -i
}

build() {
	cd "$srcdir/LHAPDF-$pkgver"
	## need to rebuild Python extension code with up-to-date Cython for Python 3.7
	## will eventually be fixed upstream
	touch wrappers/python/lhapdf.pyx
	./configure --prefix=/usr
	make
}

check() {
	cd "$srcdir/LHAPDF-$pkgver"
	make -k check
}

package() {
	cd "$srcdir/LHAPDF-$pkgver"
	make DESTDIR="$pkgdir/" install

	# If python2 is present, also build a library for it
	if [ -x /usr/bin/python2 ]; then
	  PYTHON=/usr/bin/python2 ./configure --prefix=/usr
	  make DESTDIR="$pkgdir/" install
	fi

	# make /usr/share/LHAPDF world writable, so lhapdf get works as an ordinary user
	chmod -R uog+rwX $pkgdir/usr/share/LHAPDF
}
