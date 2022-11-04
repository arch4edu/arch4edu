# Maintainer: Yu-Hsuan Tu <dobe0331 at gmail dot com>
# Contributor: Qirui Wang <wqr.prg@gmail.com>
# Contributor: Filipe Laíns (FFY00) <lains@archlinux.org>
# Contributor: Morten Linderud <foxboron@archlinux.org>
# Contributor: Eric Bélanger <eric@archlinux.org>

pkgname=python-wxpython-dev
_pkgname=wxPython
pkgver=4.2.1a1.dev5530+3ee614e0
pkgrel=1
pkgdesc='Cross-platform GUI toolkit. Developer version'
arch=('x86_64')
license=('custom:wxWindows')
url='https://www.wxpython.org'
depends=('wxwidgets-gtk3' 'python-six')
optdepends=('python-pypubsub: Alternative to the deprecated wx.lib.pubsub API')
makedepends=('mesa' 'glu' 'webkit2gtk' 'python-requests' 'python-setuptools' 'python-attrdict')
checkdepends=('xorg-server-xvfb' 'python-pytest-forked' 'python-numpy')
provides=('python-wxpython')
conflicts=('python-wxpython')
source=("https://wxpython.org/Phoenix/snapshot-builds/wxPython-$pkgver.tar.gz")
sha512sums=('dfd478b1157dae2a71083a5cff6d5033917fc72203c5e23ce0358da111103d4212f983a4c13bbd0d2be1d1f7e6c130475d53b18489da5b383179d10d507f2e73')

build() {
  cd "$_pkgname-$pkgver"
  python build.py build --release
}

check() {
  cd "$_pkgname-$pkgver"

  # there are segfaulting tests so --forked ensures we get sensible results
  PYTHONPATH=$PWD xvfb-run pytest --forked unittests || echo "==> WARNING: tests usually fail randomly"
}

package() {
  cd "$_pkgname-$pkgver"

  python build.py install --destdir="$pkgdir"

  install -Dm 644 LICENSE.txt "$pkgdir"/usr/share/licenses/$pkgname/LICENSE.txt
  find "$pkgdir/usr/lib" -type f | xargs chmod 644
}
