# $Id$
# Maintainer: psdp <psdp.dev@gmail.com>

pkgname=shadowsocksr
pkgver=3.2.2
pkgrel=1
pkgdesc="Python port of ShadowsocksR"
license=('Apache')
url="https://github.com/shadowsocksrr/shadowsocksr"
arch=('any')
depends=('python' 'python-setuptools')
makedepends=('git')
optdepends=('libsodium: For salsa20 and chacha20 support')
checkdepends=('python-coverage' 'python-pyflakes' 'libsodium' 'python-nose' 'dante' 'procps-ng' 'util-linux')
install=${pkgname}.install
conflicts=('shadowsocks')
source=("git+https://github.com/shadowsocksrr/shadowsocksr.git#tag=$pkgver"
        "shadowsocksr@.service"
        "shadowsocksr-server@.service")
sha512sums=('SKIP'
            'dd77ee24e92866e719ea67ab6dd836aef6227c0671fc42ff6bc82bbc51d8b2d5f6b90648e39d1ae3302fee073df58d14fe8ad1ac0ce636e539669683dbb58a7f'
            '8bfb42ba935bd76a7c016b220eb61ebdcee0895ca7c88644edab7c7ef840d890b3f69cf61f2cbe8eed12d9f728aa5be1d6d5c8c51e1a63e68da4f81bb1b5a583')

package() {
  cd shadowsocksr

  python setup.py install -O1 --root="$pkgdir"

  install -dm755 "$pkgdir/usr/share/man/man1"
  install -m644 debian/{ssserver.1,sslocal.1} "$pkgdir/usr/share/man/man1"
  install -Dm644 debian/config.json "$pkgdir/etc/shadowsocksr/config.json"

  install -Dm644 "$srcdir/shadowsocksr@.service" "$pkgdir/usr/lib/systemd/system/shadowsocksr@.service"
  install -Dm644 "$srcdir/shadowsocksr-server@.service" "$pkgdir/usr/lib/systemd/system/shadowsocksr-server@.service"
}
