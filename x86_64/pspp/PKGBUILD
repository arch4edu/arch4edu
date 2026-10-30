# Maintainer: Miguel Revilla <yo (at) miguelrevilla.com>
# Contributor: joyfulgirl <joyfulgirl (at) archlinux.us>
pkgname=pspp
pkgver=2.1.3
pkgrel=1
pkgdesc="Statistical analysis program. Free replacement for SPSS."
arch=('x86_64')
url="https://www.gnu.org/software/pspp/"
license=('GPL-3.0-or-later')
depends=(
  'cairo' 'cblas' 'glib2' 'glibc' 'gsl' 'gtk3' 'gtksourceview4'
  'harfbuzz' 'hicolor-icon-theme' 'libxml2' 'pango' 'postgresql-libs'
  'readline' 'spread-sheet-widget' 'zlib'
)
makedepends=('glib2-devel' 'perl' 'python')
checkdepends=('perl-text-diff')
optdepends=('xdg-utils: open the manual in a web browser')
options=('!libtool' '!emptydirs')
source=("https://ftp.gnu.org/gnu/pspp/pspp-${pkgver}.tar.gz"{,.sig})
sha256sums=('5095bc01f20f285032fb41fe757c7674e8c45dac95252663ea04670577df2727'
            'SKIP')
validpgpkeys=('C2D1AB061656AAC54B5E975485199DE8C6648E90') # Ben Pfaff

build() {
	cd "${srcdir}/${pkgname}-${pkgver}"
	./configure --prefix=/usr \
		--sysconfdir=/etc \
		--with-perl-module=yes
	make
}

check() {
	cd "${srcdir}/${pkgname}-${pkgver}"
	make check
}

package() {
	cd "${srcdir}/${pkgname}-${pkgver}"
	make DESTDIR="${pkgdir}" install
	rm -f "${pkgdir}/usr/share/info/dir"
}
