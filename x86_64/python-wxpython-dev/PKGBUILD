# Maintainer: Yu-Hsuan Tu <dobe0331 at gmail dot com>
# Contributor: Qirui Wang <wqr.prg@gmail.com>
# Contributor: Filipe Laíns (FFY00) <lains@archlinux.org>
# Contributor: Morten Linderud <foxboron@archlinux.org>
# Contributor: Eric Bélanger <eric@archlinux.org>

pkgname=python-wxpython-dev
_pkgname=wxPython
pkgver=4.1.1
pkgrel=4
pkgdesc='Cross-platform GUI toolkit. Developer version'
arch=('x86_64')
license=('custom:wxWindows')
url='https://www.wxpython.org'
depends=('wxgtk3-dev' 'python-six')
optdepends=('python-pypubsub: Alternative to the deprecated wx.lib.pubsub API')
makedepends=('mesa' 'glu' 'webkit2gtk' 'python-requests' 'python-setuptools' 'patch')
checkdepends=('xorg-server-xvfb' 'python-pytest-forked' 'python-numpy')
provides=('python-wxpython')
conflicts=('python-wxpython')
source=("https://files.pythonhosted.org/packages/source/w/wxPython/wxPython-$pkgver.tar.gz"
"aa3dca0e40bd0701e82ce40297a982b5b84844dc.patch"
"f5a55e6bf38ab5a0e7b7161477d2d523d057ec29.patch"
"d9725119d742ff25e815d0824c62abd8953a61df.patch"
"7afcc7fbc68506b55b5bb85970871a5f3df6eac4.patch"
)
sha512sums=('00924008b97bbecb824c3fffd46fc76a5a3115d9346eb95baccc6cca99c080aa80b586af42fece8a3b4d234f2d07ffa8b66b50a164c41cbd95abc9b139c32809'
'7e44c7ed5cf2688f1082dcb51e3cbaad22be67e18bb64536ec2820a3defcdc982ac0b8570b62d69157019163eaad673612708d882bb0c9105ee67ab1a4e41029'
'923a0a10c90792f3f9383c69079ab07b3254bf8d7467c8340fc3fceb21860645da75e99794dc13b3abb92bc16dedba012c730fbc507aa5e378ab3dfe60334f54'
'1627314f9ccfda1189f295a293a834559d009d5ed0ca2c5fb4d7843120341a65900dc788c747b1203279435614fa8d9341c0997553bbfffb7884d071fc5bcb49'
'd70fda4dc90fcc6cdee465fa2e96702245045e71eb5710c690a95eb1b09f3009fb5beca6dfb3d975aa38aec1926e8b603f58293073abd523f1d39a8b1d0e2b3e'
)

prepare() {
  patch -d "$_pkgname-$pkgver" -p1 < ../aa3dca0e40bd0701e82ce40297a982b5b84844dc.patch
  patch -d "$_pkgname-$pkgver" -p1 < ../f5a55e6bf38ab5a0e7b7161477d2d523d057ec29.patch
  patch -d "$_pkgname-$pkgver" -p1 < ../d9725119d742ff25e815d0824c62abd8953a61df.patch
  patch -d "$_pkgname-$pkgver" -p1 < ../7afcc7fbc68506b55b5bb85970871a5f3df6eac4.patch
  cd "$_pkgname-$pkgver"
  sed -i "s|WX_CONFIG = 'wx-config'|WX_CONFIG = 'wx-config-gtk3'|" build.py
}

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
