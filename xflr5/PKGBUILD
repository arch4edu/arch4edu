# Maintainer: Alexander Schnaidt <alex.schnaidt@gmail.com>
# Original Contributor: Gareth R <newtackdesign@gmail.com>
# Contributor: Simon K <simon@booya.at>
# Contributor: James Duley <jagduley gmail>

pkgname=xflr5
pkgver=6.47
pkgrel=1
pkgdesc="An analysis tool for airfoils, wings and planes operating at low Reynolds Numbers."
arch=('i686' 'x86_64')
url="http://www.xflr5.com/xflr5.htm"
license=('GPL')
depends=('qt5-base')
source=("https://downloads.sourceforge.net/project/xflr5/${pkgver}/xflr5_v${pkgver}_src.tar.gz")
sha256sums=('5bd936f6d0cf14b26a36d1397670943633485ba9c9f65a8ceabcd9b163caa30b')


build() {
  cd $pkgname
  
  qmake-qt5 PREFIX=/usr
  make
}

package() {
  cd $pkgname

  make INSTALL_ROOT="$pkgdir" install
}

