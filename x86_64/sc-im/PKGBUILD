# Maintainer: Rhinoceros <https://aur.archlinux.org/account/rhinoceros>
# Contributor: Rhinoceros <https://aur.archlinux.org/account/rhinoceros>

pkgname=sc-im
pkgver=0.8.4
pkgrel=1
pkgdesc='A spreadsheet program based on SC'
arch=(i686 x86_64 armv7h aarch64)
url='https://github.com/andmarti1424/sc-im'
depends=(libxml2 libzip)
optdepends=('libxlsxwriter: export to xlsx. Requires rebuild of sc-im'
            'gnuplot: create graphs')
license=(BSD)
conflicts=(scim-spreadsheet sc-im-git)
source=("$pkgname-$pkgver.tar.gz::https://github.com/andmarti1424/$pkgname/archive/v${pkgver}.tar.gz"
        ${pkgname}_arch_0.8.3.patch)
sha256sums=(ebb1f10006fe49f964a356494f96d86a4f06eb018659e3b9bde63b25c03abdf0
            2ba5a7c20d250d14a32dd3fad956779551cc18ab5f080ce149ba8395a70d0c41)

prepare() {
  cd "$pkgname-$pkgver/src"
  # install things in the correct place for package managers
  patch <"$srcdir/${pkgname}_arch_0.8.3.patch"
}

build() {
  cd "$pkgname-$pkgver/src"
  CFLAGS="-fcommon -Wp,-D_FORTIFY_SOURCE=2" make
}

package() {
  cd "$pkgname-$pkgver/src"
  make DESTDIR="$pkgdir" install

  install -D -m644 ../LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
