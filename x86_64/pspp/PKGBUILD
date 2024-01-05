# Maintainer: Miguel Revilla <yo (at) miguelrevilla.com>
# Contributor: joyfulgirl <joyfulgirl (at) archlinux.us>
pkgname=pspp
pkgver=2.0.0
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
source=("https://ftp.gnu.org/gnu/pspp/pspp-${pkgver}.tar.gz"
		"docbuild.patch::https://git.savannah.gnu.org/cgit/pspp.git/patch/?id=d8f8542df36afc05f526af2ddd1e2782d09495e3")
sha1sums=('8f858fea536f5c2c8f656d4954bfcce1c2462344'
          '50ca3cd856dc0c3acba3522e4da5b2e213b3f4e9')

prepare() {
	cd "${srcdir}/${pkgname}-${pkgver}"

	patch -p1 < ../docbuild.patch

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
