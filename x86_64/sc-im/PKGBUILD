# Maintainer: Rhinoceros <https://aur.archlinux.org/account/rhinoceros>
# Contributor: Rhinoceros <https://aur.archlinux.org/account/rhinoceros>

pkgname=sc-im
pkgver=0.8.3
pkgrel=1
pkgdesc='A spreadsheet program based on SC'
arch=('i686' 'x86_64' 'armv7h' 'aarch64')
url='https://github.com/andmarti1424/sc-im'
depends=(libxml2 libzip)
optdepends=('libxlsxwriter: export to xlsx. Requires rebuild of sc-im'
            'gnuplot: create graphs')
license=('BSD')
conflicts=('scim-spreadsheet' 'sc-im-git')
source=("$pkgname-$pkgver.tar.gz::https://github.com/andmarti1424/$pkgname/archive/v${pkgver}.tar.gz"
        "${pkgname}_arch_0.8.3.patch")
sha256sums=('5568f9987b6d26535c0e7a427158848f1bc03d829f74e41cbcf007d8704e9bd3'
            '2ba5a7c20d250d14a32dd3fad956779551cc18ab5f080ce149ba8395a70d0c41')

prepare() {
  cd "$pkgname-$pkgver/src"
  # install things in the correct place for package managers
  patch <"$srcdir/${pkgname}_arch_0.8.3.patch"
}

build() {
  cd "$pkgname-$pkgver/src"
  CFLAGS+=' -fcommon '
  make
}

package() {
  cd "$pkgname-$pkgver/src"
  make DESTDIR="$pkgdir" install

  install -D -m644 ../LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
