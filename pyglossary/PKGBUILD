# Maintainer: Julian Maingot <sikmir@gmail.com>
# Contributor: Nikolay Korotkiy <sikmir@gmail.com>

pkgname=pyglossary
pkgver=4.0.11
pkgrel=1
pkgdesc="A tool for converting dictionary files aka glossaries with various formats for different dictionary applications"
arch=(any)
url="https://github.com/ilius/pyglossary"
license=('GPL3')
# TODO add python-libzim and python-lzo if/when they exist
depends=('python')
optdepends=(
  'python-gobject: Gtk3-based interface'
  'tix: Tkinter-based interface'
  'python-lxml: Many optional flags and formats'
  'python-beautifulsoup4: HTML parsing'
  'python-yaml: Reading from cc-kedict'
  'python-pyicu: Reading or writing Aard 2 (.slob) files'
  'python-marisa: Writing to Kobo E-Reader Dictionary'
)
makedepends=('python-setuptools')
provides=("${pkgname}=${pkgver}")
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/ilius/${pkgname}/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('d56d8f8f18a33c1bc8be45571379736ae732e8f4009a1f4ac0d21ea22eb9eb01')

package() {
  cd "$srcdir/$pkgname-$pkgver"
  python setup.py install --root="$pkgdir/" --prefix=/usr --optimize=1
  cp config.json $pkgdir/usr/share/pyglossary
}

# vim:set ts=2 sw=2 et:
