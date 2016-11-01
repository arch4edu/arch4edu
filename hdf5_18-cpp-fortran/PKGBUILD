# Maintainer: Jingbei Li <i@jingbei.li>

pkgname=hdf5_18-cpp-fortran
_pkgname=hdf5
pkgver=1.8.17
pkgrel=2
arch=('i686' 'x86_64')
pkgdesc="General purpose library and file format for storing scientific data"
url="http://www.hdfgroup.org/HDF5/"
license=('custom')
depends=('zlib' 'sh' 'gcc-libs')
makedepends=('time' 'gcc-fortran')
conflicts=('hdf5')
provides=('hdf5')
source=(ftp://ftp.hdfgroup.org/HDF5/current/src/${_pkgname}-${pkgver/_/-}.tar.bz2)
sha1sums=('640f1a46cb1b353339695355b4fca42df05be765')

build() {
	cd "$srcdir/${_pkgname}-${pkgver/_/-}"
	./configure --prefix=/usr --disable-static \
		--enable-hl \
		--enable-cxx \
		--enable-fortran \
		--enable-fortran2003 \
		--enable-linux-lfs \
		--enable-build-mode=production \
		--with-pic \
		--docdir=/usr/share/doc/hdf5/ \
		--with-pthread=/usr/lib/ \
		--disable-sharedlib-rpath
	make
}

package() {
	cd "$srcdir/${_pkgname}-${pkgver/_/-}"

	make -j1 DESTDIR="${pkgdir}" install

	install -d -m755 "$pkgdir/usr/share/licenses/${pkgname}"
	install -m644 "$srcdir/${_pkgname}-${pkgver/_/-}/COPYING" \
		"$pkgdir/usr/share/licenses/${pkgname}/LICENSE"
}

