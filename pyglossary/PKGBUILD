# Maintainer: Nikolay Korotkiy <sikmir@gmail.com>
pkgname=pyglossary
pkgver=3.1.0
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
sha256sums=('00f2bc41bee56478d693c5f53ee1c7f301f36548f40b7914abba1d804769cb32'
            'd9fa86612326d5bad7d6b180bdcb7c3eb0ba56a9158425a8f474918ff4cef8ea'
            '53231fdb0c99bab8f9d12c29554b009f71efc89b7f7459d8242375be787ad026')

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
