# Maintainer: Miguel Revilla <yo (at) miguelrevilla.com>
# Contributor: joyfulgirl <joyfulgirl (at) archlinux.us>
pkgname=pspp
pkgver=2.1.1
pkgrel=1
pkgdesc="Statistical analysis program. Free replacement for SPSS."
arch=('x86_64')
url="http://www.gnu.org/software/pspp/"
license=('GPL-3.0-or-later')
depends=('gsl' 'gtk3' 'gtksourceview4' 'cairo' 'pango' 'gettext' 'zlib'
         'libxml2' 'spread-sheet-widget' 'desktop-file-utils' 'postgresql-libs')
makedepends=('python' 'glib2-devel')
checkdepends=('perl-text-diff')
optdepends=()
options=('!libtool' '!emptydirs')
source=("https://ftp.gnu.org/gnu/pspp/pspp-${pkgver}.tar.gz")
sha256sums=('b5e550937bdfa66a1e6ca729195272e8e5e66b3e04686b2d83fb2e66d4ef14c3')

build() {
	cd "${srcdir}/${pkgname}-${pkgver}"

	sed -i 's/.*_GL_EXTERN_C.*bsearch.*/#undef bsearch\n&/' gl/stdlib.in.h
	sed -i 's/.*_GL_EXTERN_C.*wmemchr.*/#undef wmemchr\n&/' gl/wchar.in.h

	./configure --prefix=/usr \
		--sysconfdir=/etc \
		--without-libreadline-prefix

	make
}

package() {
	cd "${srcdir}/${pkgname}-${pkgver}"
	make DESTDIR="${pkgdir}" install
	rm -f "${pkgdir}/usr/share/info/dir"
}

# End of file
