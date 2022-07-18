# Maintainer: Alexander Schnaidt <alex.schnaidt@gmail.com>
# Original Contributor: Gareth R <newtackdesign@gmail.com>
# Contributor: Simon K <simon@booya.at>
# Contributor: James Duley <jagduley gmail>

pkgname=xflr5
_revision=1431
_pkgver=6.57
pkgver=$_pkgver.r$_revision
pkgrel=1
pkgdesc="An analysis tool for airfoils, wings and planes operating at low Reynolds Numbers."
arch=('i686' 'x86_64')
url="http://www.xflr5.tech/xflr5.htm"
license=('GPL')
depends=('qt5-base')
makedepends=('subversion')
source=("$pkgname::svn+https://svn.code.sf.net/p/xflr5/code/#revision=$_revision")
sha256sums=('SKIP')


build() {
  cd $pkgname/tags/v$_pkgver/xflr5
  
  qmake-qt5 PREFIX=/usr
  make
}

package() {
 cd $pkgname/tags/v$_pkgver/xflr5

  make INSTALL_ROOT="$pkgdir" install
}

