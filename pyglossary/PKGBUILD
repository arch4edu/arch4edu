# Maintainer: Nikolay Korotkiy <sikmir@gmail.com>
pkgname=pyglossary
pkgver=3.2.1
pkgrel=1
pkgdesc="A tool for converting dictionary files aka glossaries with various formats for different dictionary applications"
arch=(any)
url="https://github.com/ilius/pyglossary"
license=('GPL3')
depends=('python-gobject' 'tix')
provides=("${pkgname}=${pkgver}")
conflicts=(${pkgname}-git)
source=("https://github.com/ilius/${pkgname}/archive/${pkgver}.tar.gz"
        "core.patch"
        "setup.patch")
sha256sums=('de5c9bfec56e37e2f6c1d4fbd7cc9b4dbfba5dcd471bd2af49b59393c5ea1516'
            '8d2e773ff783a7f94b67819298d3d26fde2feabc1ee425f6dc2c31d992fafec1'
            '6ac8a96f5f56bbebcdce55a077ccbcbe6b8395c5c014e820aaca09354f08da4a')

prepare() {
  cd "$srcdir/$pkgname-$pkgver"
  patch -Np1 < ../core.patch
  patch -Np1 < ../setup.patch
}

package() {
  cd "$srcdir/$pkgname-$pkgver"
  python setup.py install --root="$pkgdir/" --prefix=/usr --optimize=1
  mkdir -p $pkgdir/usr/bin
  ln -s /usr/share/pyglossary/pyglossary.pyw $pkgdir/usr/bin/pyglossary
  cp config.json $pkgdir/usr/share/pyglossary
}

# vim:set ts=2 sw=2 et:
