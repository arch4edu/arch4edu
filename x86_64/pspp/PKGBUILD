# Maintainer: Miguel Revilla <yo (at) miguelrevilla.com>
# Contributor: joyfulgirl <joyfulgirl (at) archlinux.us>
pkgname=pspp
pkgver=2.0.1
pkgrel=2
pkgdesc="Statistical analysis program. Free replacement for SPSS."
arch=('i686' 'x86_64')
url="http://www.gnu.org/software/pspp/"
license=('GPL3')
depends=('gsl' 'gtksourceview4' 'postgresql-libs' 'desktop-file-utils' 'spread-sheet-widget' 'cairo' 'pango' 'gettext')
makedepends=('python' 'glib2-devel')
optdepends=('zlib: GNUmeric support'
            'libxml2: GNUmeric support')
options=('!libtool' '!emptydirs')
source=("https://ftp.gnu.org/gnu/pspp/pspp-${pkgver}.tar.gz")
sha1sums=('58c1c949b51a6a5555a945380c8228f37814a833')

prepare() {
	cd "${srcdir}/${pkgname}-${pkgver}"

	./configure --prefix=/usr \
				--sysconfdir=/etc \
				--without-libreadline-prefix
}

build() {
    cd "${srcdir}/${pkgname}-${pkgver}"

    make CFLAGS="$CFLAGS -fcommon"
}

package() {
    cd "${srcdir}/${pkgname}-${pkgver}"
    make DESTDIR="${pkgdir}" install
    rm -f "${pkgdir}/usr/share/info/dir"
}


# End of file
