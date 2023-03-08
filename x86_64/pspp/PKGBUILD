# Maintainer: Miguel Revilla <yo (at) miguelrevilla.com>
# Contributor: joyfulgirl <joyfulgirl (at) archlinux.us>
pkgname=pspp
pkgver=1.6.2
pkgrel=1
pkgdesc="Statistical analysis program. Free replacement for SPSS."
arch=('i686' 'x86_64')
url="http://www.gnu.org/software/pspp/"
license=('GPL3')
depends=('gsl' 'gtksourceview4' 'postgresql-libs' 'desktop-file-utils' 'spread-sheet-widget' 'cairo' 'pango' 'gettext')
makedepends=('python')
optdepends=('zlib: GNUmeric support'
            'libxml2: GNUmeric support')
options=('!libtool' '!emptydirs')
source=("https://ftp.gnu.org/gnu/pspp/pspp-${pkgver}.tar.gz")
md5sums=('0e2aecdf978b9de9feb94214e39185bd')

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
