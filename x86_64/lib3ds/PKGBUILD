# Maintainer: Thomas Ascher <thomas.ascher@gmx.at>
# Contributor: Thomas Ascher <thomas.ascher@gmx.at>
pkgname=lib3ds
pkgrel=1
pkgver=1.3.0
pkgdesc="A library for managing 3D-Studio Release 3 and 4 .3DS files and a free alternative to Autodesk's 3DS File Toolkit."
arch=('i686' 'x86_64')
url="https://code.google.com/archive/p/$pkgname/"
license=('LGPL')
depends=('sh')
source=("https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/$pkgname/$pkgname-$pkgver.zip")
sha256sums=('f5b00c302955a67fa5fb1f2d3f2583767cdc61fdbc6fd843c0c7c9d95c5629e3')

build() {
  cd "$pkgname-$pkgver"
  ./configure --prefix=/usr --enable-shared
  make
}

package() {
  cd "$pkgname-$pkgver"
  make DESTDIR="$pkgdir/" install
}
