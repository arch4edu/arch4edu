# Maintainer: Raphael Isemann <teemperor@gmail.com>

pkgname=cern-vdt
pkgver=0.3.9
pkgrel=1
pkgdesc='A vectorised math library from CERN'
arch=('i686' 'x86_64')
url='https://github.com/dpiparo/vdt'
license=('LGPL3')
depends=()
makedepends=('cmake'  'git')
source=("git+git://github.com/dpiparo/vdt.git#tag=v${pkgver}")
md5sums=('SKIP')

build() {
  cd "$srcdir"/vdt

  mkdir build && cd build
  cmake .. -DCMAKE_INSTALL_PREFIX=/usr
  make
}

package() {
  cd "$srcdir"/vdt/build

  make DESTDIR="$pkgdir/" install

  install -Dm644 ../Licence.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
