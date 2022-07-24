# Maintainer: Yu-Hsuan Tu <dobe0331 at gmail dot com>
# Contributor: Qirui Wang <wqr.prg@gmail.com>
# Contributor: Filipe Laíns (FFY00) <lains@archlinux.org>
# Contributor: Morten Linderud <foxboron@archlinux.org>
# Contributor: Eric Bélanger <eric@archlinux.org>

pkgname=python-wxpython-dev
_pkgname=wxPython
pkgver=4.2.0a1.dev5449+3ac1e526
pkgrel=2
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
sha512sums=('f7fe342c70fd8fa66de67e1aeeb00290dbe2f995a4917a7bb7000d025cf5a084199bb1db6f23bc7b743448aa185f725af57aa9ed2b2ae8eead08ca69bb8e4137')

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
