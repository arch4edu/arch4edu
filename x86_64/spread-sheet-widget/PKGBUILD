# Maintainer: Miguel Revilla <yo at miguelrevilla dot com>

pkgname=spread-sheet-widget
pkgver=0.10
pkgrel=2
pkgdesc="Library for Gtk+ which provides a widget for viewing and manipulating 2 dimensional tabular data"
arch=('i686' 'x86_64')
url="https://www.gnu.org/software/ssw/"
license=("GPL3")
depends=(gtk3)
makedepends=(python glib2-devel)
source=("https://alpha.gnu.org/gnu/ssw/${pkgname}-${pkgver}.tar.gz")
sha1sums=('7ee14a5f8f18a8c88193b5ee671a1223dc3fd499')

prepare() {
	cd "${srcdir}/${pkgname}-${pkgver}"

	./configure --prefix=/usr
}

build() {
	cd "${srcdir}/${pkgname}-${pkgver}"

	make
}

package() {
	cd "${srcdir}/${pkgname}-${pkgver}"

	make DESTDIR="${pkgdir}" install
}

# End of file
