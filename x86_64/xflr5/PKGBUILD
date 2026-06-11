# Maintainer: Alexander Schnaidt <alex.schnaidt@gmail.com>
# Original Contributor: Gareth R <newtackdesign@gmail.com>
# Contributor: Simon K <simon@booya.at>
# Contributor: James Duley <jagduley gmail>

pkgname=xflr5
_revision=1505
_pkgver=6.62
pkgver=$_pkgver.r$_revision
pkgrel=1
pkgdesc="An analysis tool for airfoils, wings and planes operating at low Reynolds Numbers."
arch=('i686' 'x86_64')
url="http://www.xflr5.tech/xflr5.htm"
license=('GPL-3.0-only')
depends=('qt5-base' 'libgcc' 'glibc' 'libglvnd' 'libstdc++')
makedepends=('subversion')
source=("$pkgname-$_pkgver::svn+https://svn.code.sf.net/p/xflr5/code/trunk#revision=$_revision"
	desktop-file.patch)
sha256sums=('SKIP'
            '807ae293ae3aff263676e38a326a83dc2abed5aaba2e327f2eb42e873bfb7506')

prepare() {
  cd $pkgname-$_pkgver/xflr5

  patch -p0 < ${srcdir}/desktop-file.patch
}

build() {
  cd $pkgname-$_pkgver/xflr5
  
  qmake-qt5 PREFIX=/usr
  make
}

package() {
 cd $pkgname-$_pkgver/xflr5

  make INSTALL_ROOT="$pkgdir" install
}

